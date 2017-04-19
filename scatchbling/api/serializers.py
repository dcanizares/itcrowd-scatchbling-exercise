"""API Endpoints serializers."""
from rest_framework import serializers
from app.models import Item, Size
from serializer_fields import SizesField


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Item model."""

    sizes = SizesField(many=True, queryset=Size.objects.all())

    class Meta:
        """Meta class for serializer configuration."""

        model = Item
        fields = ('id', 'item_name', 'item_description', 'item_price', 'sizes')
        read_only_fields = ('id', )

    def create(self, validated_data):
        """Create method overrided to have read/write nested serializer."""
        sizes_data = validated_data.pop("sizes")
        item = Item.objects.create(**validated_data)
        for size_name in sizes_data:
            size_qs = Size.objects.filter(size_name=size_name)
            if size_qs.exists():
                size = size_qs.first()
            else:
                size = Size.objects.get(size_name=size_name)
            item.sizes.add(size)

        return item

    def update(self, instance, validated_data):
        """Update method overrided to have read/write nested serializer."""
        instance.item_name = validated_data.get('item_name')
        instance.item_description = validated_data.get('item_description')
        instance.item_price = validated_data.get('item_price')

        sizes_data = validated_data.pop("sizes")
        instance.sizes.clear()
        for size_name in sizes_data:
            size_qs = Size.objects.filter(size_name=size_name)
            if size_qs.exists():
                size = size_qs.first()
            else:
                size = Size.objects.get(size_name=size_name)
            instance.sizes.add(size)

        instance.save()

        return instance
