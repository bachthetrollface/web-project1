# Generated by Django 5.1.4 on 2024-12-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_cart_add_time_purchase_add_time_orderlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
