"""Pruebas E2E del módulo de autenticación (login) de Outline.

Cubre los tres tipos de caso que pide la rúbrica:
  - VÁLIDO    : la pantalla carga y un correo bien formado avanza a confirmación.
  - FRONTERA  : correo mínimo válido / formulario vacío.
  - ERROR     : correo mal formado no debe avanzar.

Incluye además una prueba data-driven con @pytest.mark.parametrize (puente con
la Parte 2 de la sección 4.3). Todas usan esperas explícitas vía los Page Objects.
"""
import pytest
from pages.login_page import LoginPage

VALID_EMAIL = "qa.tester@example.com"


def test_login_page_shows_email_field(driver, base_url):
    """VÁLIDO: la pantalla de login muestra el campo de correo."""
    page = LoginPage(driver, base_url).load()
    assert page.email_field_displayed(), "El campo de correo no es visible en el login."


def test_valid_email_shows_confirmation(driver, base_url):
    """VÁLIDO: un correo bien formado dispara la pantalla de confirmación."""
    page = LoginPage(driver, base_url).load()
    page.login_with_email(VALID_EMAIL)
    assert page.confirmation_displayed(), "No se mostró la confirmación del enlace de acceso."


def test_invalid_email_is_rejected(driver, base_url):
    """ERROR: un correo mal formado no debe llegar a la confirmación."""
    page = LoginPage(driver, base_url).load()
    page.login_with_email("esto-no-es-un-correo")
    assert not page.confirmation_displayed(), "Se aceptó un correo con formato inválido."
    assert page.still_on_login(), "La app no permaneció en la pantalla de login."


def test_empty_email_cannot_submit(driver, base_url):
    """FRONTERA/ERROR: enviar el formulario vacío no debe avanzar."""
    page = LoginPage(driver, base_url).load()
    page.login_with_email("")
    assert not page.confirmation_displayed(), "El formulario vacío no debería avanzar."
    assert page.still_on_login(), "La app no permaneció en la pantalla de login."


@pytest.mark.parametrize(
    "email, should_pass",
    [
        ("a@b.co", True),                       # FRONTERA: correo mínimo válido
        ("nombre.apellido@upa.edu.mx", True),   # VÁLIDO: formato típico
        ("sin-arroba.com", False),              # ERROR: falta el '@'
        ("@sin-local", False),                  # ERROR: sin parte local
        ("", False),                            # FRONTERA: vacío
    ],
)
def test_login_email_validation_parametrized(driver, base_url, email, should_pass):
    """DATA-DRIVEN: valida varios formatos de correo en una sola prueba."""
    page = LoginPage(driver, base_url).load()
    page.login_with_email(email)
    if should_pass:
        assert page.confirmation_displayed(), f"Se esperaba aceptar el correo: {email!r}"
    else:
        assert not page.confirmation_displayed(), f"Se esperaba rechazar el correo: {email!r}"
