# Generated by Django 4.2.3 on 2023-07-28 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('randomSongs', '0010_rename_songname_suggestions_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Suggestions',
            new_name='songSuggestons',
        ),
    ]
