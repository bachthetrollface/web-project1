from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.IntegerField("ID", primary_key=True)
    item_type = models.CharField("Type", max_length=30)
    size = models.CharField("Size", max_length=5)