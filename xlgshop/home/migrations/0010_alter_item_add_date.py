# Generated by Django 5.1.4 on 2024-12-24 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_purchase_review_specification_available_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 24, 7, 52, 5, 617886, tzinfo=datetime.timezone.utc), verbose_name='Time Added'),
        ),
    ]
