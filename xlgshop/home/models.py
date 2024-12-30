from django.db import models
from django.contrib.auth.models import User

# Create your models here.

payment_methods = [(i,i) for i in ["VNPayQR", "MoMo", "Credit Card", "ATM Card", "Debit Card"]]
item_status = [(i,i) for i in ['Not Delivered', 'Delivering', 'Received', 'Returned']]


class Category(models.Model):
    name = models.CharField("Name", max_length=20, primary_key=True)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.CharField("ID", max_length=5, primary_key=True)
    name = models.CharField("Name", max_length=50, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, blank=False, null=False)
    add_date = models.DateTimeField("Time Added")
    description = models.CharField("Description", max_length=200, default="", blank=True, null=True)
    img_path = models.CharField("Path to item's image", max_length=50, default="", blank=True, null=True)
    
    def __str__(self):
        return f"[{self.id}] {self.name}"


class ItemSpecification(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    size = models.CharField("Size", max_length=3, blank=False, null=False)
    color = models.CharField("Color", max_length=20, blank=False, null=False)
    price = models.FloatField("Price", blank=False, null=False)
    available_qty = models.IntegerField("Amount in stock", default=0, blank=True, null=True)
    sold_qty = models.IntegerField("Amount sold", default=0, blank=True, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['item', 'size', 'color'], name='primary_key'
            ),
            models.CheckConstraint(
                condition=models.Q(available_qty__gte=0), name='available_qty_nonnegative'
            ),
            models.CheckConstraint(
                condition=models.Q(sold_qty__gte=0), name='sold_qty_nonnegative'
            ),
            models.CheckConstraint(
                condition=models.Q(price__gte=0), name='price_nonnegative'
            )
        ]
    
    def __str__(self):
        return f"{self.item} - {self.size} - {self.color}"


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    price = models.FloatField("Price", blank=False, null=False)
    first_name = models.CharField("First name", max_length=20, blank=False, null=False)
    last_name = models.CharField("Last name", max_length=20, blank=False, null=False)
    phone_number = models.CharField("Phone number", max_length=15, blank=False, null=False)
    email = models.EmailField("Email", max_length=45, blank=False, null=False)
    address = models.CharField("Address", max_length=100, blank=False, null=False)
    payment_method = models.CharField("Payment method", max_length=20, blank=False, null=False, choices=payment_methods)
    add_time = models.DateTimeField("Time of purchase", auto_now_add=True)

    def __str__(self):
        return f"[{self.pk}] {self.user.username} - {self.add_time}"
    # names, phone number and email are set default as information from user; 
    # can be changed by user into information of receiver
    

class OrderList(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, blank=False, null=False)
    item = models.ForeignKey(ItemSpecification, on_delete=models.DO_NOTHING, blank=False, null=False)
    qty = models.PositiveIntegerField("Quantity", blank=False, null=False)
    status = models.CharField("Status", max_length=20, blank=False, null=False, choices=item_status)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['purchase', 'item'], name="purchase_and_item_unique"
            )
        ]
    
    def __str__(self):
        return f"{self.purchase} - {self.item}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=False, null=False)
    rating = models.PositiveIntegerField("Rating", default=5)
    review = models.CharField("Review", max_length=200, default="", blank=True, null=True)
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(rating__lte=5), name='rating_between_0_and_5'
            )
        ]
    
    def __str__(self):
        return f"{self.pk}. {self.item}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    item = models.ForeignKey(ItemSpecification, on_delete=models.CASCADE, blank=False, null=False)
    qty = models.PositiveIntegerField("Quantity", blank=False, null=False)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'item'], name="user_and_item_unique"
            )
        ]
    
    def __str__(self):
        return f"{self.user.username}: {self.item} x{self.qty}"