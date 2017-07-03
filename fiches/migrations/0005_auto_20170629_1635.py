# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0004_auto_20170629_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='avant_garde',
            name='avants',
            field=models.SmallIntegerField(choices=[(1, b'Ambidextre'), (2, b'Attaque rapide'), (3, b'Attaque \xc3\xa9clair'), (4, b'Blas\xc3\xa9'), (5, b'Bon tireur'), (6, b'Bonne r\xc3\xa9putation'), (7, b'Charge berserk'), (8, b'Cible rapide'), (9, b'Combat aveugle'), (10, b'Constitution solide'), (11, b'Contre attaque'), (12, b'Coup infaillible'), (13, b'Discipline de fer'), (14, b'Endurci'), (15, b'D\xc3\xa9cadence'), (16, b'D\xc3\xa9sarmement'), (17, b'Grand orateur'), (18, b'Grand praticien'), (19, b'G\xc3\xa9nie'), (20, b'Haine (nom de la race)'), (21, b'Imitation'), (22, b'Litanie de haine'), (23, b'Ma\xc3\xaetre du combat'), (24, b'Elu du n\xc3\xa9ant'), (25, b'Pas de c\xc3\xb4t\xc3\xa9'), (26, b'Sans peur'), (27, b'Sens aiguis\xc3\xa9 (nom du sens)'), (28, b'Sommeil l\xc3\xa9ger'), (29, b'Tir double'), (30, b'Tir en mouvement'), (31, b'Vivacit\xc3\xa9'), (32, b'Voix troublante'), (33, b'Aucun')], default=33),
        ),
        migrations.AddField(
            model_name='avant_garde',
            name='desavants',
            field=models.SmallIntegerField(choices=[(1, b'Boiteux'), (2, b'D\xc3\xa9rang\xc3\xa9'), (3, b'Borgne'), (4, b'Doigt perdu'), (5, b"Peur (nom de la race ou de l'animal)"), (6, b'Nerveux'), (7, b'L\xc3\xa2che'), (8, b'Appr\xc3\xa9cie (Tol\xc3\xa8re pour les morts-vivants) les (orcs, sorciers, trolls, elfes de sang, morts-vivants)'), (9, b'Malchanceux'), (10, b'Maladroit'), (11, b'D\xc3\xa9bile'), (12, b'Sommeil lourd'), (13, b'Lourdaud'), (14, b'\xc3\x82me damn\xc3\xa9e'), (15, b'Mauvaise r\xc3\xa9putation'), (16, b'Maladif'), (17, b'Constitution faible'), (18, b'Faible r\xc3\xa9sistance'), (19, b"D\xc3\xa9pendance (nom du type d'alcool/drogue)"), (20, b'Aucun')], default=20),
        ),
        migrations.AddField(
            model_name='avant_garde',
            name='equipement',
            field=models.CharField(blank=True, default=b'Sans', max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='avant_garde',
            name='inventaire',
            field=models.CharField(blank=True, default=b'Sans', max_length=800, null=True),
        ),
    ]