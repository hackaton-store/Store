# Generated by Django 4.2.1 on 2023-06-06 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank_card', '0005_alter_bankcard_card_holder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcard',
            name='card_holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
