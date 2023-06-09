# Generated by Django 4.2.2 on 2023-06-06 06:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(choices=[('Another', 'Another'), ('Toyota', 'Toyota'), ('Mercedes', 'Mercedes'), ('BMW', 'Bmw'), ('Audi', 'Audi')], default='Another', max_length=100)),
                ('color', models.CharField(choices=[('Another', 'Another'), ('R', 'Red'), ('B', 'Blue'), ('G', 'Green'), ('Y', 'Yellow'), ('BK', 'Black'), ('WH', 'White'), ('SV', 'Silver'), ('GR', 'Gray')], default='Another', max_length=40)),
                ('release', models.IntegerField(validators=[django.core.validators.MaxValueValidator(2023, 'Date cannot be above 2023'), django.core.validators.MinValueValidator(1900, 'Date cannot be below 1900')])),
                ('image', models.ImageField(upload_to='cars')),
            ],
        ),
    ]
