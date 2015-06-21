# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0008_auto_20141228_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fiche',
            name='autresprenoms',
        ),
        migrations.RemoveField(
            model_name='fiche',
            name='autrestitres',
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom2',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom3',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom4',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom5',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom6',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom7',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='prenom8',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='profession',
            field=models.CharField(default=b'prostipute', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre2',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre3',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre4',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre5',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre6',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre7',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='fiche',
            name='titre8',
            field=models.CharField(default=b'', max_length=75),
            preserve_default=True,
        ),
    ]
