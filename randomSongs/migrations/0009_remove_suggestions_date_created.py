# Generated by Django 4.2.3 on 2023-07-28 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomSongs', '0008_delete_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suggestions',
            name='date_created',
        ),
    ]
