from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.helpers import URL
from selenium.webdriver.common.by import By


class Login_Page:

    _INPUT_DE_USERNAME = (By.NAME, 'user-name')
    _INPUT_DE_PASSWORD = (By.NAME, 'password')
    _LOGIN_BUTTON = (By.ID,'login-button')

    def __init__(self, driver):
     self.driver = driver

    def navegar_a_url_login(self):
        self.driver.get(URL)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_DE_USERNAME)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_DE_PASSWORD)
        ).send_keys(password)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)
        ).click()


        

   
   
