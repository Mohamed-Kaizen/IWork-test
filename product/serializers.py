"""Collection serializers."""
from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Item serializer."""

    id = serializers.CharField(read_only=True)

    slug = serializers.CharField(read_only=True)

    created_at = serializers.DateTimeField(read_only=True)

    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        """Meta data."""

        model = Item
        fields = (
            "id",
            "name",
            "quantity",
            "slug",
            "created_at",
            "updated_at",
        )
