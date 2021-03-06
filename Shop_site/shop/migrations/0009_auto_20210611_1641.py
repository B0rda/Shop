# Generated by Django 3.2.3 on 2021-06-11 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20210528_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='hozproduct',
            name='v_nal',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='hozproduct',
            name='percent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='hozproduct',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='percent',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='v_nal',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=4),
        ),
    ]
