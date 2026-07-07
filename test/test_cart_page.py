import pytest
from page.login_page import Login_Page
from page.inventario_page import inventario_page
from page.cart_page import CartPage
import time
from utils.helpers import USUARIO_VALIDO, PASSWORD_VALIDO


def test_cart_operations(driver):
    login = Login_Page(driver)
    inventory = inventario_page(driver)
    cart = CartPage(driver)

    login.navegar_a_url_login()
    login.login(USUARIO_VALIDO, PASSWORD_VALIDO)

    time.sleep(3)
    # Agregar producto e ir al carrito
    inventory.agregar_producto_al_carrito()
    inventory.ir_al_carrito()

    assert cart.is_at_page()
    assert cart.get_cart_items_count() == 1

    # Continuar comprando
    cart.continue_shopping()
    assert inventory.en_pagina_de_inventario()


def test_remove_from_cart(driver):
    login = Login_Page(driver)
    inventory = inventario_page(driver)
    cart = CartPage(driver)

    login.navegar_a_url_login()
    login.login(USUARIO_VALIDO, PASSWORD_VALIDO)
    time.sleep(3)

    inventory.agregar_producto_al_carrito()
    inventory.ir_al_carrito()

    initial_count = cart.get_cart_items_count()
    cart.remove_item(0)

    assert cart.get_cart_items_count() == initial_count -1



