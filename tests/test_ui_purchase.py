from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_flujo_inventario_completo(page: Page):
    login = LoginPage(page)
    inventory = InventoryPage(page)

    login.navegar()
    login.realizar_login("standard_user", "secret_sauce")

    # Validamos cantidad de items usando POM
    assert inventory.obtener_cantidad_items() == 6

    # Agregamos al carrito
    inventory.agregar_primer_item_al_carrito()
    assert inventory.obtener_conteo_carrito() == "1"
