# Generated by Django 5.0 on 2023-12-28 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_customer_products_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
