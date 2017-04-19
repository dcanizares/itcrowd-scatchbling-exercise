from rest_framework import viewsets
from app.models import Item
from serializers import ItemSerializer


class ItemViewSet(viewsets.ModelViewSet):
    """CRUD API endpoint for items."""

    queryset = Item.objects.all()
    serializer_class = ItemSerializer
