import re
import os
import logging
import pathlib
import pytest

from utils.helpers import get_driver

# Definimos las rutas partiendo desde la ubicación de este conftest.py
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent
LOG_DIR = PROJECT_ROOT / "logs"
SCREENSHOT_DIR = PROJECT_ROOT / "reporte" / "screenshots"

# Creamos las carpetas de logs y reportes automáticamente si no existen
LOG_DIR.mkdir(exist_ok=True)
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

# Logger básico para el historial de la API
logging.basicConfig(
    filename=LOG_DIR / "historial.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger_api = logging.getLogger("Logs-de-testeo-api")


def historial(mensaje):
    print(mensaje)
    logger_api.info(mensaje)


def configurar_logger(name="automation_ui"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(sh)
    return logger


def tomar_screenshot(driver, name: str):
    # Guarda la captura física con extensión .png en la carpeta reporte/screenshots
    path = SCREENSHOT_DIR / f"{name}_{int(__import__('time').time())}.png"
    driver.save_screenshot(str(path))
    return path


@pytest.fixture
def logger():
    return configurar_logger("automation_ui")


@pytest.fixture
def driver(request, logger):
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        logger = item.funcargs.get("logger")
        
        if driver is not None:
            safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
            screenshot_path = tomar_screenshot(driver, safe_name)
            
            if logger is not None:
                logger.error("Fallo detectado. Captura guardada en %s", screenshot_path)
            
            html = item.config.pluginmanager.getplugin('html')
            if html is not None:
                # 1. Usamos 'extras' en lugar de 'extra' (saca el DeprecationWarning)
                extras = getattr(rep, 'extras', [])
                
                # 2. Usamos una ruta relativa simple (saca el UserWarning del reporte auto-contenido)
                ruta_relativa = os.path.relpath(screenshot_path, start=PROJECT_ROOT)
                
                extras.append(html.extras.image(str(ruta_relativa)))
                rep.extras = extras