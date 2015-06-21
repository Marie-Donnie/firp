# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0002_auto_20141227_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='sexe',
            field=models.BooleanField(default=True, choices=[(True, b'Homme'), (False, b'Femme')]),
        ),
    ]
