# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-14 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0028_auto_20170714_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quete',
            name='difficulte',
            field=models.SmallIntegerField(choices=[(1, b'Facile'), (2, b'Moyenne'), (3, b'Difficile'), (4, b'Tr\xc3\xa8s difficile'), (5, b'Suicidaire'), (6, b'Inconnue')], default=2),
        ),
    ]