# Generated by Django 3.2.3 on 2021-06-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210615_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hozproduct',
            name='Type',
            field=models.BooleanField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='Type',
            field=models.BooleanField(default=0, editable=False),
        ),
    ]
