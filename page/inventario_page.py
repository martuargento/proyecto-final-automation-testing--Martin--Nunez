from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class inventario_page:
    URL_CURRENT = 'inventory.html'
    MENU_BUTTON = (By.ID, 'react-burger-menu-btn')
    LINK_BUTTON = (By.ID, 'logout_sidebar_link')

    def __init__(self, driver):
        self.driver = driver

    def en_pagina_de_inventario(self):
        return self.URL_CURRENT in self.driver.current_url
    
    def agregar_producto_al_carrito(self):
        self.driver.find_element(By.CLASS_NAME, 'btn_small').click()
        # btn_agregar_pruducto_al_carrito = self.driver.find_element(By.CLASS_NAME, 'btn_inventory')
        # btn_agregar_pruducto_al_carrito.click()

    def ir_al_carrito(self):
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
        # btn_ir_al_carrito = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        # btn_ir_al_carrito.click()
    
    def logout(self):
        self.driver.find_element(*self.MENU_BUTTON).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        ).click()


