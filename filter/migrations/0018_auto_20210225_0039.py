# Generated by Django 3.1.2 on 2021-02-24 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter', '0017_auto_20210225_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_name',
            field=models.FloatField(),
        ),
    ]
