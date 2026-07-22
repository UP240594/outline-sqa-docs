"""Page Object del módulo de búsqueda de Outline (requiere sesión activa).

Mismo criterio de localizadores que ``LoginPage``: por atributo/rol/texto, no
por clase. Verificar contra la instancia real los marcados con ``# VERIFICAR``.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage


class SearchPage(BasePage):
    PATH = "/search"

    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        'input[type="search"], input[placeholder*="Search"], input[placeholder*="Buscar"]',
    )  # VERIFICAR
    # Los resultados de Outline son enlaces a documentos (/doc/...).
    RESULT_ITEMS = (
        By.CSS_SELECTOR,
        'a[href*="/doc/"], [data-testid="search-result"]',
    )  # VERIFICAR
    EMPTY_STATE = (
        By.XPATH,
        '//*[contains(translate(., "NO RESULTS", "no results"), "no results") '
        'or contains(., "Sin resultados") or contains(., "No documents")]',
    )  # VERIFICAR

    # ---- acciones de negocio ---------------------------------------
    def load(self):
        return self.open(self.PATH)

    def search(self, query):
        field = self.visible(self.SEARCH_INPUT)
        field.clear()
        field.send_keys(query)
        field.send_keys(Keys.ENTER)
        return self

    # ---- aserciones de estado --------------------------------------
    def has_results(self):
        return self.is_visible(self.RESULT_ITEMS, timeout=10)

    def result_count(self):
        return self.count(self.RESULT_ITEMS) if self.has_results() else 0

    def empty_state_displayed(self):
        return self.is_visible(self.EMPTY_STATE, timeout=10)
