from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_login_exitoso_pom(page: Page):
    login = LoginPage(page)
    login.navegar()
    login.realizar_login("standard_user", "secret_sauce")

    # Evidence capture
    page.screenshot(path="screenshots/login_exitoso_pom.png")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_login_fallido_pom(page: Page):
    login = LoginPage(page)
    login.navegar()
    login.realizar_login("usuario_incorrecto", "clave_incorrecta")

    # Evidence capture
    page.screenshot(path="screenshots/error_login_pom.png")
    expect(login.error_message).to_be_visible()
    expect(login.error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service")
