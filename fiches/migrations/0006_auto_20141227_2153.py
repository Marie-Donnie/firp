# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0005_auto_20141227_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='zone_naissance',
            field=models.SmallIntegerField(choices=[(b"Royaumes de l'est", [(0, b'Bois de la P\xc3\xa9nombre'), (1, b'Bois des Chants \xc3\xa9ternels'), (2, b'Cap Strangleronce'), (3, b'Clairi\xc3\xa8res de Tirisfal'), (4, b'Contreforts de Hautebrande'), (5, b'Dun Morogh'), (6, b'D\xc3\xa9fil\xc3\xa9 de Deuillevent'), (7, b"For\xc3\xaat d'Elwynn"), (8, b'For\xc3\xaat des Pins-Argent\xc3\xa9s'), (9, b'Giln\xc3\xa9as'), (10, b'Gorge des Vents br\xc3\xbblants'), (11, b'Hautes-terres Arathies'), (12, b'Hautes-terres du Cr\xc3\xa9puscule'), (13, b"Kul'Tiras"), (14, b'Les Carmines'), (15, b'Les Hinterlands'), (16, b'Les Paluns'), (17, b'Les terres Fant\xc3\xb4mes'), (18, b'Loch Modan'), (19, b"Maleterres de l'Est"), (20, b"Maleterres de l'Ouest"), (21, b'Marais des Chagrins'), (22, b"Marche de l'Ouest"), (23, b'Noirebois'), (24, b'Steppes Ardentes'), (25, b'Strangleronce septentrionale'), (26, b'Terres Foudroy\xc3\xa9es'), (27, b'Terres Ingrates'), (28, b"\xc3\x8ele de Quel'Danas")]), (b'Kalimdor', [(100, b'Azshara'), (101, b"Berceau-de-l'Hiver"), (102, b"Crat\xc3\xa8re d'Un'Goro"), (103, b'Durotar'), (104, b'D\xc3\xa9solace'), (105, b'F\xc3\xa9ralas'), (106, b'Gangrebois'), (107, b'Les Serres-Rocheuses'), (108, b"Mar\xc3\xa9cage d'\xc3\x82prefange"), (109, b'Mille pointes'), (110, b'Mont Hyjal'), (111, b'Mulgore'), (112, b'Orneval'), (113, b'Reflet-de-Lune'), (114, b'Silithus'), (115, b'Sombrivage'), (116, b'Tanaris'), (117, b'Tarides du Nord'), (118, b'Tarides du Sud'), (119, b'Teldrassil'), (120, b'Uldum'), (121, b"\xc3\x8eles de l'\xc3\x89cho")]), (b'Norfendre', [(200, b'Bassin de Sholazar'), (201, b'D\xc3\xa9solation des dragons'), (202, b'Fjord Hurlant'), (203, b'For\xc3\xaat du Chant de cristal'), (204, b"Joug-d'hiver"), (205, b'La Couronne de glace'), (206, b'Les Grisonnes'), (207, b'Les pics Foudroy\xc3\xa9s'), (208, b'Toundra Bor\xc3\xa9enne'), (209, b"Zul'Drak")])]),
        ),
    ]
