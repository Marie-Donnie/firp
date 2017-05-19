# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-19 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0030_auto_20170518_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiche',
            old_name='aff_createur',
            new_name='afficher_createur',
        ),
        migrations.RenameField(
            model_name='fiche',
            old_name='aff_inventaire',
            new_name='afficher_inventaire',
        ),
        migrations.RenameField(
            model_name='fiche',
            old_name='pseudo',
            new_name='pseudo_du_personnage',
        ),
        migrations.AddField(
            model_name='fiche',
            name='afficher_pseudo',
            field=models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=True),
        ),
    ]
