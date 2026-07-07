import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"


def get_driver():
    opciones_chrome = Options()

    # Configuración del modo de ejecución
    if os.getenv("CI") == "true":
        opciones_chrome.add_argument("--headless=new")
    else:
        opciones_chrome.add_argument("--start-maximized")

    # Configuración general del navegador
    opciones_chrome.add_argument("--incognito")
    opciones_chrome.add_argument("--window-size=1400,800")

    # Opciones de estabilidad
    opciones_chrome.add_argument("--no-sandbox")
    opciones_chrome.add_argument("--disable-dev-shm-usage")
    opciones_chrome.add_argument("--disable-gpu")

    # Configuración de logs
    opciones_chrome.add_argument("--log-level=3")
    opciones_chrome.add_experimental_option(
        "excludeSwitches", ["enable-logging"]
    )

    driver = webdriver.Chrome(options=opciones_chrome)

    driver.implicitly_wait(2)

    return driver