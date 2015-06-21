# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0009_auto_20141228_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiche',
            name='description',
            field=models.CharField(default=b'A venir', max_length=3000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='historique',
            field=models.CharField(default=b'A venir', max_length=3000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='fiche',
            name='profession',
            field=models.CharField(default=b'Prostipute', max_length=75),
        ),
    ]
