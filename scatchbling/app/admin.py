from django.contrib import admin

# Register your models here.
from .models import Item, Size

admin.site.register(Item)
admin.site.register(Size)
