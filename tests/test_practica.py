from playwright.sync_api import sync_playwright


def run_test():
    with sync_playwright() as p:
        # Lanzamos el navegador visible (headless=False)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("Navegando a Google...")
        page.goto("https://www.google.com")

        # Obtenemos el título
        titulo = page.title()
        print(f"¡Conexión exitosa! El título es: {titulo}")

        # Sacamos una captura de pantalla
        page.screenshot(path="evidencia_google.png")
        print("Captura de pantalla guardada.")

        browser.close()


if __name__ == "__main__":
    run_test()
