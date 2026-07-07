import pytest
from page.login_page import Login_Page
from page.inventario_page import inventario_page
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
from page.checkout_complete_page import CheckoutCompletePage
import time
from utils.helpers import USUARIO_VALIDO, PASSWORD_VALIDO


def test_complete_purchase_flow(driver):
    login = Login_Page(driver)
    inventory = inventario_page(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    checkout_complete = CheckoutCompletePage(driver)

    # Login
    login.navegar_a_url_login()
    login.login(USUARIO_VALIDO, PASSWORD_VALIDO)

    time.sleep(4)

    # Agregar producto al carrito
    inventory.agregar_producto_al_carrito()
    inventory.ir_al_carrito()

    time.sleep(4)

    # Ir a checkout
    cart.go_to_checkout()
    time.sleep(3)

    # Llenar información de checkout
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()
    
    # Apretar boton para finalizar la compra
    checkout_complete.finalizar_compra()

    # Verificar página de checkout complete
    assert checkout_complete.is_at_page()
    assert "Thank you for your order!" in checkout_complete.get_success_message()
    assert checkout_complete.is_success_message_displayed()
    
    # Volver al inicio
    checkout_complete.back_to_home()
    assert inventory.en_pagina_de_inventario()




    