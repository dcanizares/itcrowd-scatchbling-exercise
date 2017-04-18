from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=200)
    item_price = models.FloatField(default=0)


class Size(models.Model):
    size_name = models.CharField(max_length=5)
    size_description = models.CharField(max_length=50)


class ItemSize(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
