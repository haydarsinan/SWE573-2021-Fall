# Generated by Django 3.2.8 on 2021-11-30 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicEventPool', '0002_auto_20211130_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_provider',
            field=models.TextField(blank=True, null=True),
        ),
    ]
