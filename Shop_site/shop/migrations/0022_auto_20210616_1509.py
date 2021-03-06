# Generated by Django 3.2.3 on 2021-06-16 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20210616_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zakazcart',
            name='hozproduct',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='shop.hozproduct'),
        ),
        migrations.AlterField(
            model_name='zakazcart',
            name='product',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.PROTECT, to='shop.product'),
        ),
    ]
