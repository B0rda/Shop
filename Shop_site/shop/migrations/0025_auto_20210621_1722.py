# Generated by Django 3.2.3 on 2021-06-21 14:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_auto_20210621_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hozproduct',
            name='percent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='percent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
