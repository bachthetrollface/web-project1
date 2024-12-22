from django.db import models

# Create your models here.

"""
1 relation for each type of item,
1 size relation for each item type above,
items store availability of sizes: has_s, has_m, has_l, has_xl,...,
colors?: different ids for different colors
relations for storing available colors

table for saving purchases
"""

class Category(models.Model):
    name = models.CharField("Name", max_length=20, primary_key=True)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.CharField("ID", max_length=5, primary_key=True)
    name = models.CharField("Name", max_length=30, blank=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, blank=False)
    add_date = models.DateTimeField("Time Added")
    description = models.CharField("Description", max_length=200, default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} - {self.name}"


class Specification(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    size = models.CharField("Size", max_length=3)
    color = models.CharField("Color", max_length=20)
    price = models.FloatField("Price", blank=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item', 'size', 'color'], name='primary_key'
            )
        ]
    
    def __str__(self):
        return f"{self.item.__str__()} - {self.size} - {self.color}"
