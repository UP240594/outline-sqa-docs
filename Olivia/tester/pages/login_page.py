"""Page Object de la pantalla de autenticación (login) de Outline.

IMPORTANTE sobre los localizadores
----------------------------------
Outline está construido con React + styled-components, por lo que las clases
CSS son hasheadas e inestables. Por eso aquí se localiza por ATRIBUTOS
(``type``, ``name``, ``placeholder``) y por TEXTO/rol, no por clase. Aun así,
el equipo DEBE verificar cada localizador contra su instancia real
(Inspeccionar elemento) y ajustarlo si su versión de Outline difiere.
Los marcados con ``# VERIFICAR`` son los más sensibles a cambios de versión.
"""
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # En self-hosted, la raíz redirige al login cuando no hay sesión.
    PATH = "/"

    # Outline muestra primero botones de proveedor; el de correo revela el campo.
    EMAIL_TOGGLE = (
        By.XPATH,
        '//button[contains(., "Email") or contains(., "correo") or contains(., "Correo")]',
    )  # VERIFICAR
    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        'input[type="email"], input[name="email"]',
    )
    SUBMIT_BUTTON = (
        By.XPATH,
        '//button[@type="submit" or contains(., "Sign In") or contains(., "Continue") '
        'or contains(., "Continuar") or contains(., "Iniciar")]',
    )  # VERIFICAR
    # Pantalla "te enviamos un enlace mágico".
    CONFIRMATION = (
        By.XPATH,
        '//*[contains(translate(., "CHECK", "check"), "check your email") '
        'or contains(., "revisa tu correo") or contains(., "enlace")]',
    )  # VERIFICAR

    # ---- acciones de negocio ---------------------------------------
    def load(self):
        return self.open(self.PATH)

    def _reveal_email_field(self):
        """Si el campo de correo no está visible, hace clic en el botón de correo."""
        if not self.is_visible(self.EMAIL_INPUT, timeout=3):
            try:
                self.clickable(self.EMAIL_TOGGLE).click()
            except Exception:
                pass  # algunas versiones muestran el campo directamente
        return self

    def login_with_email(self, email):
        """Captura un correo y envía el formulario de acceso por enlace."""
        self._reveal_email_field()
        field = self.visible(self.EMAIL_INPUT)
        field.clear()
        if email:
            field.send_keys(email)
        self.clickable(self.SUBMIT_BUTTON).click()
        return self

    # ---- aserciones de estado --------------------------------------
    def email_field_displayed(self):
        self._reveal_email_field()
        return self.is_visible(self.EMAIL_INPUT)

    def confirmation_displayed(self):
        return self.is_visible(self.CONFIRMATION, timeout=8)

    def still_on_login(self):
        """True si seguimos en la pantalla de login (no se avanzó)."""
        return self.is_visible(self.EMAIL_INPUT, timeout=3) or "/login" in self.driver.current_url
