# Generated by Django 3.1.2 on 2021-02-24 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0006_auto_20210224_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='item_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
