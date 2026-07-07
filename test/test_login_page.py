import pytest
from page.login_page import Login_Page
from utils.example_csv import get_csv_data, get_json_data
from utils.faker import get_login_faker
from utils.helpers import USUARIO_VALIDO, PASSWORD_VALIDO

@pytest.mark.parametrize("username, password, login_booleano", get_login_faker())

def test_login(driver, username, password, login_booleano):
    
    loginPage = Login_Page(driver)
    loginPage.navegar_a_url_login()
    loginPage.login(username, password)
    
    if login_booleano:
        assert "inventory.html" in driver.current_url
    else:
        assert "inventory.html" not in driver.current_url



        