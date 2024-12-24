from django.contrib import admin
from .models import Item, Category, ItemSpecification, Purchase, Review

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(ItemSpecification)
admin.site.register(Purchase)
admin.site.register(Review)

# Purchase and Review only included for easy database observation, should only add such records through front-end inputs