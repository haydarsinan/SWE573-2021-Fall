# Generated by Django 3.2.8 on 2022-01-10 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ServicEventPool', '0027_auto_20220110_1245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='event',
        ),
    ]
