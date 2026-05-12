from playwright.sync_api import Page, expect


def test_saucedemo_health_check(page: Page):
    """
    Smoke Test: Verifica que el sitio principal responda y 
    que los elementos base del DOM estén presentes.
    """
    print("\n[SMOKE TEST] Verificando salud de SauceDemo...")

    # 1. Acceso al sitio
    page.goto("https://www.saucedemo.com/")

    # 2. Validación de Título y URL
    expect(page).to_have_title("Swag Labs")
    expect(page).to_have_url("https://www.saucedemo.com/")

    # 3. Verificación de elementos críticos de UI (Login Form)
    # Si esto falla, ni siquiera intentamos el resto de la suite
    login_button = page.get_by_role("button", name="Login")
    expect(login_button).to_be_visible()

    # 4. Captura técnica de salud
    page.screenshot(path="screenshots/health_check_saucedemo.png")

    print("[SMOKE TEST] Sistema operativo y listo para pruebas.")
