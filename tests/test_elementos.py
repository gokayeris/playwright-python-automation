from playwright.sync_api import Page, expect


def test_componentes_complejos(page: Page):
    print("Iniciando sesión para probar elementos...")
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    # --- 1. MANEJO DE DROPDOWN (SELECT) ---
    dropdown = page.locator("[data-test='product-sort-container']")
    dropdown.select_option("lohi")

    # Verify first item price
    first_price = page.locator(".inventory_item_price").first
    expect(first_price).to_contain_text("7.99")

    # --- 2. MANEJO DE LISTAS Y CONTEO ---
    productos = page.locator(".inventory_item")
    expect(productos).to_have_count(6)
    print(f"Se verificaron {productos.count()} productos en total.")

    # --- 3. DEBUGGING MODE ---
    # Uncomment the line below if you need to inspect elements manually
    # page.pause()
