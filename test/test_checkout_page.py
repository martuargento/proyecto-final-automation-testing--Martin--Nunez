import pytest
from page.login_page import Login_Page
from page.inventario_page import inventario_page
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage
import time
from utils.helpers import USUARIO_VALIDO, PASSWORD_VALIDO


def test_checkout_process(driver):
    login = Login_Page(driver)
    inventory = inventario_page(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.navegar_a_url_login()
    login.login(USUARIO_VALIDO, PASSWORD_VALIDO)
    time.sleep(4)

    inventory.agregar_producto_al_carrito()
    inventory.ir_al_carrito()
    time.sleep(4)
    cart.go_to_checkout()
    time.sleep(3)

    assert checkout.is_at_page()

    # Llenar información de checkout
    checkout.fill_customer_info("John", "Doe", "12345")
    checkout.continue_to_overview()

    assert "checkout-step-two" in driver.current_url


def test_checkout_validation(driver):
    login = Login_Page(driver)
    inventory = inventario_page(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.navegar_a_url_login()
    login.login(USUARIO_VALIDO, PASSWORD_VALIDO)
    time.sleep(4)

    inventory.agregar_producto_al_carrito()
    inventory.ir_al_carrito()
    time.sleep(4)
    cart.go_to_checkout()
    time.sleep(3)

    # Intentar continuar sin llenar información
    checkout.continue_to_overview()

    # Verificar que se muestre mensaje de error
    error_message = checkout.get_error_message()
    assert "First Name is required" in error_message



    