# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0019_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=b'images/site/no-image.png', upload_to=b'images/users/'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='image',
            field=models.ImageField(default=b'images/site/no-image.png', upload_to=b'images/persos/'),
        ),
    ]