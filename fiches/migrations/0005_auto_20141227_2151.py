# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0004_auto_20141227_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='pj',
            field=models.CharField(max_length=1, choices=[(b'p', b'Personnage jou\xc3\xa9'), (b'a', b'Personnage jouable'), (b'n', b'Personnage non jou\xc3\xa9')]),
        ),
    ]
