# Generated by Django 5.0.4 on 2024-05-26 08:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mangacard',
            old_name='genre',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='mangacard',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='mangacard',
            name='image_url',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mangacard',
            name='isbn',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mangacard',
            name='publisher',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mangacard',
            name='year_of_publication',
            field=models.IntegerField(default=0),
        ),
    ]
