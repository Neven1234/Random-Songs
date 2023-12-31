# Generated by Django 4.2.3 on 2023-07-28 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('randomSongs', '0006_suggestions_delete_songsugge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='p1.png', null=True, upload_to='')),
                ('email', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
