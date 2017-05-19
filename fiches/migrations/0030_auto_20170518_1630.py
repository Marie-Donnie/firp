# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0029_auto_20170517_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='image',
            field=models.ImageField(default=b'images/site/no-image.png', upload_to=b'images/persos'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default=b'images/site/no-image.png', upload_to=b'images/users'),
        ),
    ]