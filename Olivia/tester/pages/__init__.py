"""Paquete de Page Objects para la suite E2E de Outline."""
from .base_page import BasePage
from .login_page import LoginPage
from .search_page import SearchPage

__all__ = ["BasePage", "LoginPage", "SearchPage"]
