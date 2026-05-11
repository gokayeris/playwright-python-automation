from playwright.sync_api import sync_playwright, expect


def run_test():
    with sync_playwright() as p:
        # Abrimos el navegador
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Abriendo la web de pruebas...")
        page.goto("https://www.saucedemo.com/")

        # 1. Login con contraseña inválida
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("wrong_password")
        page.get_by_role("button", name="Login").click()

        # 2. Validación de error
        error_message = page.locator("[data-test='error']")
        expect(error_message).to_be_visible()
        expect(error_message).to_have_text(
            "Epic sadface: Username and password do not match any user in this service")

        print("¡Test exitoso! El mensaje de error se mostró correctamente.")
        page.screenshot(path="evidencia_error_login.png")

        browser.close()


if __name__ == "__main__":
    run_test()
