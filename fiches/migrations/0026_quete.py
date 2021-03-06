# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0025_auto_20170712_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=75)),
                ('objectif', models.CharField(max_length=200)),
                ('cible', models.CharField(default=b'Aucune', max_length=75)),
                ('requis', models.CharField(default=b'Rien', max_length=100)),
                ('zone', models.SmallIntegerField(choices=[(b"Royaumes de l'est", [(0, b'Bois de la P\xc3\xa9nombre'), (1, b'Bois des Chants \xc3\xa9ternels'), (2, b'Cap Strangleronce'), (3, b'Clairi\xc3\xa8res de Tirisfal'), (4, b'Contreforts de Hautebrande'), (5, b'Dun Morogh'), (6, b'D\xc3\xa9fil\xc3\xa9 de Deuillevent'), (7, b"For\xc3\xaat d'Elwynn"), (8, b'For\xc3\xaat des Pins-Argent\xc3\xa9s'), (9, b'Giln\xc3\xa9as'), (10, b'Gorge des Vents br\xc3\xbblants'), (11, b'Hautes-terres Arathies'), (12, b'Hautes-terres du Cr\xc3\xa9puscule'), (13, b"Kul'Tiras"), (14, b'Les Carmines'), (15, b'Les Hinterlands'), (16, b'Les Paluns'), (17, b'Les terres Fant\xc3\xb4mes'), (18, b'Loch Modan'), (19, b"Maleterres de l'Est"), (20, b"Maleterres de l'Ouest"), (21, b'Marais des Chagrins'), (22, b"Marche de l'Ouest"), (23, b'Noirebois'), (24, b'Steppes Ardentes'), (25, b'Strangleronce septentrionale'), (26, b'Terres Foudroy\xc3\xa9es'), (27, b'Terres Ingrates'), (28, b"\xc3\x8ele de Quel'Danas")]), (b'Kalimdor', [(100, b'Azshara'), (101, b"Berceau-de-l'Hiver"), (102, b"Crat\xc3\xa8re d'Un'Goro"), (103, b'Durotar'), (104, b'D\xc3\xa9solace'), (105, b'F\xc3\xa9ralas'), (106, b'Gangrebois'), (107, b'Les Serres-Rocheuses'), (108, b"Mar\xc3\xa9cage d'\xc3\x82prefange"), (109, b'Mille pointes'), (110, b'Mont Hyjal'), (111, b'Mulgore'), (112, b'Orneval'), (113, b'Reflet-de-Lune'), (114, b'Silithus'), (115, b'Sombrivage'), (116, b'Tanaris'), (117, b'Tarides du Nord'), (118, b'Tarides du Sud'), (119, b'Teldrassil'), (120, b'Uldum'), (121, b"\xc3\x8eles de l'\xc3\x89cho")]), (b'Norfendre', [(200, b'Bassin de Sholazar'), (201, b'D\xc3\xa9solation des dragons'), (202, b'Fjord Hurlant'), (203, b'For\xc3\xaat du Chant de cristal'), (204, b"Joug-d'hiver"), (205, b'La Couronne de glace'), (206, b'Les Grisonnes'), (207, b'Les pics Foudroy\xc3\xa9s'), (208, b'Toundra Bor\xc3\xa9enne'), (209, b"Zul'Drak")]), (b'Pandarie', [(300, b'D\xc3\xa9sert de Tanlong'), (301, b'Etendues sauvages de Krasarang'), (302, b'La for\xc3\xaat de Jade'), (303, b'Sommet de Kun-Lai'), (304, b"Terres de l'Angoisse"), (305, b"Val de l'Eternel Printemps"), (306, b'Vall\xc3\xa9e des Quatre vents')]), (b'Iles bris\xc3\xa9es', [(400, b'Azsuna'), (401, b'Haut-Roc'), (402, b'Suramar'), (403, b'Tornheim'), (404, b"Val'Sharah")]), (b'Kezan', [(500, b'Kezan')]), (b'Zandalar', [(600, b'Zandalar')])], default=23, null=True)),
                ('localisation', models.CharField(max_length=75)),
                ('x', models.SmallIntegerField(default=0)),
                ('y', models.SmallIntegerField(default=0)),
                ('nb_combattants', models.SmallIntegerField(default=1)),
                ('difficulte', models.SmallIntegerField(choices=[(1, b'Facile'), (2, b'Moyenne'), (3, b'Difficile'), (4, b'Tr\xc3\xa8s difficile'), (5, b'Suicidaire')], default=2)),
                ('recompense', models.CharField(default=b'Aucune', max_length=100)),
                ('gloire', models.SmallIntegerField(default=0)),
                ('accomplie', models.BooleanField(choices=[(True, b'Oui'), (False, b'Non')], default=False)),
                ('ennemi', models.ImageField(default=b'images/site/quest/Portraits/FollowerPortrait_NoPortrait.png', upload_to=b'images/site/quest')),
                ('leader', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quete_reussie', to='fiches.Fiche')),
                ('reservee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quete_reservee', to='fiches.Fiche')),
            ],
            options={
                'ordering': ['nom', 'difficulte'],
                'verbose_name_plural': 'qu\xeates',
                'default_related_name': 'quete',
                'verbose_name': 'qu\xeate',
                'permissions': (('quete_ok', 'Peut prendre des qu\xeates'),),
            },
        ),
    ]
