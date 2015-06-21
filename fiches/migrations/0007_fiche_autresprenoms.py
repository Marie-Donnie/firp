# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0006_auto_20141227_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='fiche',
            name='autresprenoms',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
