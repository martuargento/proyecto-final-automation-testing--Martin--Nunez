from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    URL_PATH = '/checkout-complete.html'
    SUCCESS_HEADER = (By.CLASS_NAME, 'complete-header')
    BACK_HOME_BUTTON = (By.ID, 'back-to-products')
    FINISH_BUTTON = (By.ID, 'finish')

    def __init__(self, driver):
        self.driver = driver

    def is_at_page(self):
        # Verifica si la URL actual contiene el path de finalización
        return self.URL_PATH in self.driver.current_url
    
    def finalizar_compra(self):
        #apretamos el boton para finalizar la compra
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_success_message(self):
        # Retorna el texto del encabezado (ej. "Thank you for your order!")
        try:
            return self.driver.find_element(*self.SUCCESS_HEADER).text
        except:
            return ""

    def is_success_message_displayed(self):
        # Verifica si el mensaje de éxito es visible
        return self.driver.find_element(*self.SUCCESS_HEADER).is_displayed()

    def back_to_home(self):
        # Hace clic en el botón para volver a la tienda
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BACK_HOME_BUTTON)
        ).click()


