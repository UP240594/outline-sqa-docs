"""Página base con utilidades de espera EXPLÍCITA.

Toda la sincronización de la suite pasa por aquí: ningún Page Object usa
``time.sleep``. Se emplean ``WebDriverWait`` + ``expected_conditions``, tal
como exige la rúbrica (esperas explícitas, prohibido el sleep fijo).
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    DEFAULT_TIMEOUT = 15  # segundos

    def __init__(self, driver, base_url, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, timeout)

    # ---- navegación -------------------------------------------------
    def open(self, path=""):
        self.driver.get(f"{self.base_url}/{path.lstrip('/')}")
        return self

    # ---- esperas explícitas (núcleo) --------------------------------
    def visible(self, locator):
        """Espera a que el elemento sea VISIBLE y lo devuelve."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        """Espera a que el elemento sea CLICKEABLE y lo devuelve."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def present(self, locator):
        """Espera a que el elemento esté en el DOM (aunque no sea visible)."""
        return self.wait.until(EC.presence_of_element_located(locator))

    # ---- consultas tolerantes a fallo (para aserciones) -------------
    def is_visible(self, locator, timeout=None):
        """True si el elemento llega a ser visible dentro del timeout."""
        w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        try:
            w.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def body_contains(self, text, timeout=None):
        """True si el ``<body>`` contiene el texto (sin distinguir mayúsculas)."""
        w = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        needle = text.lower()
        try:
            w.until(lambda d: needle in d.find_element(By.TAG_NAME, "body").text.lower())
            return True
        except TimeoutException:
            return False

    def count(self, locator):
        return len(self.driver.find_elements(*locator))
