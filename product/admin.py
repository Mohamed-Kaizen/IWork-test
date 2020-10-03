"""Admin module for product app."""
from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Configure the product app in admin page."""

    list_display = (
        "name",
        "quantity",
        "slug",
        "created_at",
    )

    list_filter = ("updated_at",)

    date_hierarchy = "created_at"

    search_fields = ("name",)
