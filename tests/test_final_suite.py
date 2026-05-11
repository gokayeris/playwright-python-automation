import pytest
from playwright.sync_api import Page, expect

# Definimos una fixture para el login


@pytest.fixture(scope="function")
def login_sauce(page: Page):
    print("\n[Setup] Realizando login...")
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    return page

# Ahora los tests son mucho más simples:


def test_purchase_flow(login_sauce):
    page = login_sauce
    # Ya estamos logueados, vamos directo a la acción
    page.locator("[data-test='product-sort-container']").select_option("lohi")
    expect(page.locator(".inventory_item_price").first).to_contain_text("7.99")
    print("[Test] Flujo de compra verificado.")


def test_check_inventory_count(login_sauce):
    page = login_sauce
    # Validamos que haya 6 productos
    productos = page.locator(".inventory_item")
    expect(productos).to_have_count(6)
    print("[Test] Cantidad de productos verificada.")
