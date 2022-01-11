# Generated by Django 3.2.8 on 2022-01-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServicEventPool', '0028_remove_comment_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='geoLocation',
            field=models.CharField(blank=True, default='41.083556 29.050598', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='location',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]