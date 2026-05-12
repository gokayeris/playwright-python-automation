import pytest
from playwright.sync_api import Page, Playwright
from pages.login_page import LoginPage # Importar arriba es más limpio

@pytest.fixture
def login(page: Page):
    """Fixture que devuelve la página de inventario ya logueada"""
    login_page = LoginPage(page)
    login_page.navegar()
    login_page.realizar_login("standard_user", "secret_sauce")
    return login_page 

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()