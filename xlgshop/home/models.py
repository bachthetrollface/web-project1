from django.db import models

# Create your models here.

"""
table for saving purchases

"""

class Category(models.Model):
    name = models.CharField("Name", max_length=20, primary_key=True)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.CharField("ID", max_length=5, primary_key=True)
    name = models.CharField("Name", max_length=30, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, blank=False, null=False)
    add_date = models.DateTimeField("Time Added")
    description = models.CharField("Description", max_length=200, default="", blank=True, null=True)
    
    def __str__(self):
        return f"{self.id} - {self.name}"


class Specification(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    size = models.CharField("Size", max_length=3, blank=False, null=False)
    color = models.CharField("Color", max_length=20, blank=False, null=False)
    price = models.FloatField("Price", blank=False)
    available_count = models.IntegerField("Amount in stock", default=0, blank=True, null=True)
    sold_count = models.IntegerField("Amount sold", default=0, blank=True, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item', 'size', 'color'], name='primary_key'
            ),
            models.CheckConstraint(
                condition=models.Q(available_count__gte=0), name='available_count_nonnegative'
            ),
            models.CheckConstraint(
                condition=models.Q(sold_count__gte=0), name='sold_count_nonnegative'
            ),
            models.CheckConstraint(
                condition=models.Q(price__gte=0), name='price_nonnegative'
            )
        ]
    
    def __str__(self):
        return f"{self.item.__str__()} - {self.size} - {self.color}"


class Purchase(models.Model):
    name = models.CharField("Name", max_length=30, blank=False, null=False)
    email = models.EmailField("Email", max_length=50, blank=False, null=False)
    price = models.FloatField("Price", blank=False, null=False)
    # save number of items bought?


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    rating = models.IntegerField("Rating", default=5)
    review = models.CharField("Review", max_length=200, default="", blank=True, null=True)
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(rating__lte=5) & models.Q(rating__gte=0), name='rating_between_0_and_5'
            )
        ]