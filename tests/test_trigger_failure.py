import pytest
from playwright.sync_api import Page, expect


@pytest.mark.xfail(reason="Validación intencional de captura de evidencia (Screenshots/Video)")
def test_evidence_capture_check(page: Page):
    """
    Este test falla a propósito para asegurar que el sistema de 
    evidencia visual esté operativo.
    """
    page.goto("https://www.saucedemo.com/")
    # Forzamos el fallo
    expect(page).to_have_title(
        "Titulo Incorrecto para Probar Evidencia", timeout=3000)
