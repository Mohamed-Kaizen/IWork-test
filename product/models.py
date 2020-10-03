"""Collection of model."""
from typing import Any

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .utils import unique_slug


class Item(models.Model):
    """Reference item model."""

    name = models.CharField(verbose_name=_("name"), max_length=100)

    quantity = models.PositiveIntegerField(verbose_name=_("quantity"))

    slug = models.SlugField(verbose_name=_("slug"), unique=True, blank=True)

    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)

    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    class Meta:
        """Meta data."""

        verbose_name = _("item")
        verbose_name_plural = _("items")

    def __str__(self: "Item") -> str:
        """It return readable name for the model."""
        return f"{self.name}"


@receiver(pre_save, sender=Item)
def item_slug_creator(sender: Item, instance: Item, **kwargs: Any) -> None:
    """Slug generator for single for item."""
    if not instance.slug:
        instance.slug = unique_slug(title=instance.name)
