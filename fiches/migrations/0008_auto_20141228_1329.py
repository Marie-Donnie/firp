# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0007_fiche_autresprenoms'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiche',
            name='autrestitres',
            field=models.CharField(default=b'', max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
    ]
