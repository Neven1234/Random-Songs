# Generated by Django 4.2.3 on 2023-07-28 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomSongs', '0003_song_link_song_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='songSugge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
