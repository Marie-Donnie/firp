# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-28 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0002_avant_garde_classe'),
    ]

    operations = [
        migrations.AddField(
            model_name='apothicaire',
            name='perso',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apothicaire', to='fiches.Avant_garde'),
        ),
        migrations.AddField(
            model_name='fantassin',
            name='perso',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fantassin', to='fiches.Avant_garde'),
        ),
    ]
