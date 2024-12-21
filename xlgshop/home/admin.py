from django.contrib import admin
from .models import Item, Type, AvailableSizeAndColor

# Register your models here.
admin.site.register(Item)
admin.site.register(Type)
admin.site.register(AvailableSizeAndColor)