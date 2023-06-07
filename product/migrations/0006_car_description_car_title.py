# Generated by Django 4.2.2 on 2023-06-07 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_car_created_at_car_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default=None, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
    ]