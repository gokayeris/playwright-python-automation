from playwright.sync_api import sync_playwright, expect


def run_test():
    with sync_playwright() as p:
        # Abrimos el navegador
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Abriendo la web de pruebas...")
        page.goto("https://www.saucedemo.com/")

        # 1. Login (Sintaxis limpia de Playwright)
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # 2. Validación de entrada
        # Verificamos que el título de la sección sea 'Products'
        header = page.locator(".title")
        expect(header).to_have_text("Products")

        # 3. Interacción: Agregar al carrito el primer producto
        print("Agregando producto al carrito...")
        page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

        # 4. Verificación del carrito (Assertion de contador)
        badge = page.locator(".shopping_cart_badge")
        expect(badge).to_have_text("1")

        print("¡Test exitoso! Login y compra verificada.")
        page.screenshot(path="evidencia_compra.png")

        browser.close()


if __name__ == "__main__":
    run_test()

