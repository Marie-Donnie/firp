# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0012_desavantages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avant_garde',
            name='avants',
        ),
        migrations.AddField(
            model_name='avant_garde',
            name='avants',
            field=models.ManyToManyField(null=True, to='fiches.Avantages'),
        ),
        migrations.RemoveField(
            model_name='avant_garde',
            name='desavants',
        ),
        migrations.AddField(
            model_name='avant_garde',
            name='desavants',
            field=models.ManyToManyField(null=True, to='fiches.Desavantages'),
        ),
    ]