# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0003_auto_20141227_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='pj',
            field=models.CharField(max_length=1, choices=[(b'p', b'PJ'), (b'n', b'PNJ')]),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='sexe',
            field=models.CharField(max_length=1, choices=[(b'h', b'Homme'), (b'f', b'Femme')]),
        ),
    ]
