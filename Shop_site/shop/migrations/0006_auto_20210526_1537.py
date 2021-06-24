# Generated by Django 3.2.3 on 2021-05-26 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210525_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='HozCathegory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='cathegory',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop.cathegory'),
        ),
        migrations.AlterField(
            model_name='hozproduct',
            name='cathegory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.hozcathegory'),
        ),
    ]
