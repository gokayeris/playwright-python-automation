from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_items = page.locator(".inventory_item")
        self.add_to_cart_buttons = page.locator("button[id^='add-to-cart']")
        self.shopping_cart_badge = page.locator(".shopping_cart_badge")

    def obtener_cantidad_items(self):
        return self.inventory_items.count()

    def agregar_primer_item_al_carrito(self):
        self.add_to_cart_buttons.first.click()

    def obtener_conteo_carrito(self):
        return self.shopping_cart_badge.text_content()
