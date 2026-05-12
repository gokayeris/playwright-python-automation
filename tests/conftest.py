import pytest
from playwright.sync_api import Page, Playwright
from pages.login_page import LoginPage  # Importar arriba es más limpio
from datetime import datetime
import os


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


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    # Usamos report.extras para compatibilidad con versiones nuevas
    extras = getattr(report, "extras", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.failed or xfail):
            page = item.funcargs.get("page")
            if page:
                if not os.path.exists("screenshots"):
                    os.makedirs("screenshots")

                file_name = f"screenshots/{report.nodeid.replace('::', '_').replace('/', '_')}.png"
                page.screenshot(path=file_name)

                if os.path.exists(file_name):
                    # Incrustamos la imagen directamente en Base64 para que el HTML sea 100% autocontenido
                    import base64
                    with open(file_name, "rb") as image_file:
                        encoded_string = base64.b64encode(
                            image_file.read()).decode()

                    html = f'<div><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
                        f'style="width:304px;height:228px;" onclick="window.open(this.src)" align="right"/></div>'
                    extras.append(pytest_html.extras.html(html))
        report.extras = extras
