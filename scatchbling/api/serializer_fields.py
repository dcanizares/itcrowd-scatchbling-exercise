"""Custom serializer fields."""

from rest_framework import serializers
from app.models import Size


class SizesField(serializers.RelatedField):
    """Field to serialize sizes collection."""

    def to_representation(self, value):
        """DRF internal method implementation to serialize size data."""
        return value.size_name

    def to_internal_value(self, size_name):
        """DRF internal method implementation to unserialize size data."""
        size_qs = Size.objects.filter(size_name=size_name)
        if size_qs.exists():
            size = size_qs.first()
        else:
            size = Size.objects.get(size_name=size_name)

        return size
