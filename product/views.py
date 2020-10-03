"""Collection views."""
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Item
from .serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """ViewSet for Item model."""

    queryset = Item.objects.all()

    filter_backends = (OrderingFilter, SearchFilter)

    search_fields = ("name",)

    ordering = ("-created_at",)

    ordering_fields = ("name", "quantity", "created_at", "updated_at")

    lookup_field = "slug"

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = ItemSerializer
