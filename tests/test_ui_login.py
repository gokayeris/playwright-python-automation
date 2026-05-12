from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_fallido_pom(page: Page):
    login = LoginPage(page)
    login.navegar()
    login.realizar_login("usuario_invalido", "clave_falsa")

    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_contain_text(
        "Username and password do not match")


def test_login_exitoso_pom(page: Page):
    login = LoginPage(page)
    login.navegar()
    login.realizar_login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
