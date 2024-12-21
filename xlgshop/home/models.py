from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.CharField("ID", max_length=5, primary_key=True)
    item_name = models.CharField("Name", max_length=30)
    item_type = models.CharField("Type", max_length=30)
    size = models.CharField("Size", max_length=5)
    add_date = models.DateTimeField("Time Added")