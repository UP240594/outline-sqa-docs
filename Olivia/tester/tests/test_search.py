"""Pruebas E2E del módulo de búsqueda de Outline (requieren sesión).

Cubre los tres tipos de caso:
  - VÁLIDO    : un término existente devuelve resultados.
  - ERROR     : un término inexistente muestra el estado vacío.
  - FRONTERA  : una búsqueda de un solo carácter no rompe la interfaz.

Estas pruebas usan la fixture ``authenticated_driver``; si no hay cookie de
sesión configurada, se SALTAN automáticamente (no fallan).
"""
from pages.search_page import SearchPage

# Ajustar a un término que SÍ exista en su instancia (p. ej. un documento semilla).
EXISTING_TERM = "Hola"


def test_search_existing_term_returns_results(authenticated_driver, base_url):
    """VÁLIDO: buscar un término existente devuelve al menos un resultado."""
    page = SearchPage(authenticated_driver, base_url).load()
    page.search(EXISTING_TERM)
    assert page.has_results(), f"No hubo resultados para un término existente: {EXISTING_TERM!r}"


def test_search_nonexistent_term_shows_empty_state(authenticated_driver, base_url):
    """ERROR: un término inexistente muestra el estado vacío."""
    page = SearchPage(authenticated_driver, base_url).load()
    page.search("zxqwk-termino-inexistente-987654")
    assert page.empty_state_displayed(), "No se mostró el estado vacío para una búsqueda sin coincidencias."


def test_search_single_character_boundary(authenticated_driver, base_url):
    """FRONTERA: una búsqueda de un solo carácter no debe romper la UI."""
    page = SearchPage(authenticated_driver, base_url).load()
    page.search("a")
    # Resultado aceptable: o hay resultados, o se muestra el estado vacío.
    assert page.has_results() or page.empty_state_displayed(), \
        "La búsqueda de un carácter dejó la UI en un estado inesperado."
