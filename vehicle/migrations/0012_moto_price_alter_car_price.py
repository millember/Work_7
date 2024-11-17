# Generated by Django 5.1.2 on 2024-11-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_rename_amount_car_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='moto',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='цена'),
        ),
    ]
