from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Size(models.Model):
    size_name = models.CharField(max_length=5)
    size_description = models.CharField(max_length=50)

    def __unicode__(self):
        return self.size_name


class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_description = models.CharField(max_length=200)
    item_price = models.FloatField(default=0)
    sizes = models.ManyToManyField(Size)

    def __unicode__(self):
        return "{name}: {description}".format(
            name=self.item_name,
            description=self.item_description
        )
