# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-13 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0026_quete'),
    ]

    operations = [
        migrations.AddField(
            model_name='quete',
            name='creation',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
