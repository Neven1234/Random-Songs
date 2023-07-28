# Generated by Django 4.2.3 on 2023-07-28 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomSongs', '0005_rename_name_songsugge_sname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songName', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='songSugge',
        ),
    ]
