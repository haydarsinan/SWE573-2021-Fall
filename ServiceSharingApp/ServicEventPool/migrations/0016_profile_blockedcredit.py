# Generated by Django 3.2.8 on 2022-01-05 21:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicEventPool', '0015_auto_20220105_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blockedCredit',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(15), django.core.validators.MinValueValidator(1)]),
        ),
    ]
