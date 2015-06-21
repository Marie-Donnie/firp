# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='sexe',
            field=models.BooleanField(choices=[(True, b'Homme'), (False, b'Femme')]),
        ),
    ]
