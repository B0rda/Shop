# Generated by Django 3.2.3 on 2021-05-26 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210526_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cathegory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.cathegory'),
        ),
    ]