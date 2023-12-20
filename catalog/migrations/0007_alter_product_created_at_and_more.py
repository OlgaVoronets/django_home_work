# Generated by Django 5.0 on 2023-12-19 18:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 19, 18, 51, 48, 413850), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_changed_at',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 12, 19, 18, 51, 48, 413850), null=True, verbose_name='Последнее изменение'),
        ),
    ]