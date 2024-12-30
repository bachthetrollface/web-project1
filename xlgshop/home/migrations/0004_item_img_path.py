# Generated by Django 5.1.4 on 2024-12-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='img_path',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name="Path to item's image"),
        ),
    ]