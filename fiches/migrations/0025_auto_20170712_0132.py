# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-11 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0024_auto_20170712_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avant_garde',
            name='campagne',
            field=models.ManyToManyField(blank=True, to='fiches.Campagne'),
        ),
    ]