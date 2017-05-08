# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import fiches.models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0017_auto_20170505_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='annee_naissance',
            field=fiches.models.IntegerRangeField(default=b'0'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='autresprenoms',
            field=models.CharField(default=b'Aucun', max_length=200),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='autrestitres',
            field=models.CharField(default=b'Aucun', max_length=500),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='jour_naissance',
            field=fiches.models.IntegerRangeField(default=b'1'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='mois_naissance',
            field=fiches.models.IntegerRangeField(default=b'1'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='poids',
            field=models.FloatField(default=b'70'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='sexe',
            field=models.CharField(choices=[(b'h', b'Masculin'), (b'f', b'F\xc3\xa9minin')], default=b'Masculin', max_length=1),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='taille',
            field=models.FloatField(default=b'1.70'),
        ),
    ]
