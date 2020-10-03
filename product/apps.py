"""Core app for product app."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProductConfig(AppConfig):
    """Class representing a Django application and its configuration."""

    name = "product"
    verbose_name = _("Product")
