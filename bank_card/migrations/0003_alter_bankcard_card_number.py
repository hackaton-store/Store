# Generated by Django 4.2.1 on 2023-06-05 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_card', '0002_alter_bankcard_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankcard',
            name='card_number',
            field=models.BigIntegerField(),
        ),
    ]
