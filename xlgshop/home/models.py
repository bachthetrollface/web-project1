from django.db import models

# Create your models here.

# class Item(models.Model):
#     item_id = models.CharField("ID", max_length=5, primary_key=True)
#     item_name = models.CharField("Name", max_length=30)
#     item_type = models.CharField("Type", max_length=30)
#     size = models.CharField("Size", max_length=5)
#     add_date = models.DateTimeField("Time Added")

"""
1 relation for each type of item,
1 size relation for each item type above,
items store availability of sizes: has_s, has_m, has_l, has_xl,...,
colors?: different ids for different colors
relations for storing available colors
"""

class TShirt(models.Model):
    pass

class Trousers(models.Model):
    pass

class Hoodie(models.Model):
    pass

class Jeans(models.Model):
    pass

class Sweater(models.Model):
    pass

class AvailableColorsTShirt(models.Model):
    item_type = models.ForeignKey(TShirt, on_delete=models.CASCADE, primary_key=True)
    color = models.CharField("Color", primary_key=True)

class AvailableColorsTrousers(models.Model):
    item_type = models.ForeignKey(Trousers, on_delete=models.CASCADE, primary_key=True)
    color = models.CharField("Color", primary_key=True)

class AvailableColorsHoodie(models.Model):
    item_type = models.ForeignKey(Hoodie, on_delete=models.CASCADE, primary_key=True)
    color = models.CharField("Color", primary_key=True)

class AvailableColorsJeans(models.Model):
    item_type = models.ForeignKey(Jeans, on_delete=models.CASCADE, primary_key=True)
    color = models.CharField("Color", primary_key=True)

class AvailableColorsSweater(models.Model):
    item_type = models.ForeignKey(Sweater, on_delete=models.CASCADE, primary_key=True)
    color = models.CharField("Color", primary_key=True)