# Generated by Django 4.2.7 on 2024-01-15 16:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_verify_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='verify_code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Код вeрификации'),
        ),
    ]