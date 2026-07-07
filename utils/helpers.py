from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://www.saucedemo.com/"
USUARIO_VALIDO = "standard_user"
PASSWORD_VALIDO = "secret_sauce"

def get_driver():
    # Configuramos las opciones para el navegador
    opciones_chrome = Options()

    # ========================================================
    # MODO OCULTO: True = Oculto (Headless) / False = Visible
    # ========================================================
    MODO_OCULTO = False 
    
    if MODO_OCULTO:
        # Usa el motor moderno de Chrome sin interfaz gráfica
        opciones_chrome.add_argument("--headless=new")
    else:
        # Solo maximiza la ventana si el navegador va a ser visible
        opciones_chrome.add_argument("--start-maximized")

    # --- 1. SILENCIAR TERMINAL ---
    opciones_chrome.add_argument('--log-level=3')
    opciones_chrome.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 2. MODO INCÓGNITO
    opciones_chrome.add_argument("--incognito")

    # 4. Argumentos de estabilidad (evitan cierres inesperados en segundo plano)
    opciones_chrome.add_argument("--no-sandbox")
    opciones_chrome.add_argument("--disable-dev-shm-usage")
    opciones_chrome.add_argument("--disable-gpu")

    # --- 5. TAMAÑO DE VENTANA --- 
    # Es fundamental dejar un tamaño fijo en modo oculto para que Selenium "sepa" dónde clickear
    opciones_chrome.add_argument("--window-size=1400,800")

    # 6. Inicializamos el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=opciones_chrome)

    # Espera implícita para dar un margen pequeño de carga a los elementos
    driver.implicitly_wait(2)

    return driver