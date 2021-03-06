# Generated by Django 3.2.3 on 2021-06-21 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20210621_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hozproduct',
            name='percent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='percent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)]),
        ),
    ]
