# Generated by Django 5.1.2 on 2024-11-18 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_product_sold_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sold_quantity',
        ),
    ]
