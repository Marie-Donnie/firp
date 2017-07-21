# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import fiches.functions


class Migration(migrations.Migration):

    dependencies = [
        ('fiches', '0030_auto_20170714_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apothicaire',
            name='guerisseur',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='apothicaire',
            name='guerisseur_enfum',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Maître guérisseur'), (3, 'Enfumeur')]),
        ),
        migrations.AlterField(
            model_name='apothicaire',
            name='scalpel_fioles',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Maîtrise du scalpel'), (3, 'Art du lancer de fioles')]),
        ),
        migrations.AlterField(
            model_name='arbaletrier',
            name='as_du_tir',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='arbaletrier',
            name='maitr_arba',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='arbaletrier',
            name='visee_prec',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='armure',
            name='autres_effets',
            field=models.CharField(default='Aucun', max_length=100),
        ),
        migrations.AlterField(
            model_name='armure',
            name='effet',
            field=models.CharField(default='Aucun', max_length=100),
        ),
        migrations.AlterField(
            model_name='armure',
            name='effet_ig',
            field=models.CharField(default='Aucun', max_length=100),
        ),
        migrations.AlterField(
            model_name='armure',
            name='membre',
            field=models.SmallIntegerField(default=5, choices=[(1, 'Main principale'), (2, 'Autre main'), (3, 'Tête'), (4, 'Epaules'), (5, 'Torse'), (6, 'Mains'), (7, 'Taille'), (8, 'Jambes'), (9, 'Pieds'), (10, 'Dos'), (11, 'Cou'), (12, 'Doigt'), (13, 'Poignets'), (14, 'Divers'), (15, 'Arme de secours')]),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='annee_de_naissance',
            field=fiches.functions.IntegerRangeField(default='0'),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='autre_metier',
            field=models.CharField(default='Aucun', max_length=30),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='blessures',
            field=models.CharField(null=True, default='Sans', max_length=800, blank=True),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='classe',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Fantassin'), (2, 'Arbalétrier'), (3, 'Eclaireur'), (4, 'Apothicaire de combat'), (5, 'Apprenti sorcier')]),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='dependances',
            field=models.CharField(null=True, default='Sans', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='equipement',
            field=models.CharField(null=True, default='Sans', max_length=800, blank=True),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='etat',
            field=models.CharField(default='Vivant', choices=[('v', 'Vivant'), ('m', 'Mort'), ('d', 'Disparu')], max_length=1),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='ex_prof',
            field=models.SmallIntegerField(default=9, choices=[(1, 'Forgeron'), (2, 'Chasseur'), (3, 'Cuisinier'), (4, 'Tavernier'), (5, "Facteur d'arc"), (6, 'Tanneur'), (7, 'Architecte'), (8, 'Ebéniste'), (9, 'Autre métier')]),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='grade_rp',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Soldat'), (2, 'Caporal'), (3, 'Sergent'), (4, 'Lieutenant'), (5, 'Capitaine')]),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='image',
            field=models.ImageField(upload_to='images/persos', default='images/site/no-image.png'),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='inventaire',
            field=models.CharField(null=True, default='Sans', max_length=800, blank=True),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='jour_de_naissance',
            field=fiches.functions.IntegerRangeField(default='1'),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='mois_de_naissance',
            field=fiches.functions.IntegerRangeField(default='1'),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='peur',
            field=models.CharField(null=True, default='Sans', max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='pj',
            field=models.CharField(default='Personnage joué', choices=[('p', 'Personnage joué'), ('n', 'Personnage non joué')], max_length=1),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='race',
            field=models.CharField(default='Humain', choices=[('n', 'Nain'), ('e', 'Haut-elfe'), ('h', 'Humain')], max_length=1),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='sexe',
            field=models.CharField(default='Homme', choices=[('h', 'Homme'), ('f', 'Femme')], max_length=1),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='troubles_ment',
            field=models.CharField(null=True, default='Sans', max_length=800, blank=True),
        ),
        migrations.AlterField(
            model_name='avant_garde',
            name='ville_de_naissance',
            field=models.CharField(default='Inconnue', max_length=50),
        ),
        migrations.AlterField(
            model_name='avantages',
            name='nom',
            field=models.CharField(default='Aucun', max_length=50),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='annee_debut',
            field=fiches.functions.IntegerRangeField(default='37'),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='annee_fin',
            field=fiches.functions.IntegerRangeField(default='37'),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='fini',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='image',
            field=models.ImageField(upload_to='images/rpg/campagne', default='images/site/avant-garde.jpg'),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='mois_debut',
            field=fiches.functions.IntegerRangeField(default='1'),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='mois_fin',
            field=fiches.functions.IntegerRangeField(default='1'),
        ),
        migrations.AlterField(
            model_name='campagne',
            name='objectif',
            field=models.CharField(default='Tuer.', max_length=100),
        ),
        migrations.AlterField(
            model_name='desavantages',
            name='nom',
            field=models.CharField(default='Aucun', max_length=50),
        ),
        migrations.AlterField(
            model_name='eclaireur',
            name='aigle_vif',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, "Œil d'aigle"), (3, 'Vif')]),
        ),
        migrations.AlterField(
            model_name='eclaireur',
            name='silen_rodeur',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Art de la mort silencieuse'), (3, 'Rôdeur')]),
        ),
        migrations.AlterField(
            model_name='eclaireur',
            name='vigilant_rx',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Vigilant'), (3, 'Réflexes éclaireurs')]),
        ),
        migrations.AlterField(
            model_name='equipement',
            name='nom',
            field=models.CharField(default='Equipement ', max_length=50),
        ),
        migrations.AlterField(
            model_name='fantassin',
            name='athle_resi',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Athlétisme'), (3, 'Résistant')]),
        ),
        migrations.AlterField(
            model_name='fantassin',
            name='epe_craned',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Epéiste'), (3, 'Crâne dûr')]),
        ),
        migrations.AlterField(
            model_name='fantassin',
            name='feroce_impla',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Féroce'), (3, 'Implacable')]),
        ),
        migrations.AlterField(
            model_name='fantassin',
            name='glaive_lourde',
            field=models.SmallIntegerField(default=1, choices=[(1, 'Niveau inférieur'), (2, 'Maîtriste du glaive'), (3, "Maîtrise de l'armure lourde")]),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='afficher_createur',
            field=models.BooleanField(default=True, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='afficher_inventaire',
            field=models.BooleanField(default=True, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='afficher_pseudo',
            field=models.BooleanField(default=True, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='annee_de_naissance',
            field=fiches.functions.IntegerRangeField(default='0'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='autres_prenoms',
            field=models.CharField(default='Aucun', max_length=200),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='autres_titres',
            field=models.CharField(default='Aucun', max_length=500),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='c_cheveux',
            field=models.CharField(default='Brun', max_length=30),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='c_yeux',
            field=models.CharField(default='Marron', max_length=30),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='description',
            field=models.CharField(default='A venir', max_length=6000),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='etat',
            field=models.CharField(default='VI', choices=[('VI', 'Vivant'), ('MO', 'Mort'), ('DI', 'Disparu')], max_length=2),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='historique',
            field=models.CharField(default='A venir', max_length=6000),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='image',
            field=models.ImageField(upload_to='images/persos', default='images/site/no-image.png'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='inventaire',
            field=models.CharField(null=True, default='A venir', max_length=6000, blank=True),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='jour_de_naissance',
            field=fiches.functions.IntegerRangeField(default='1'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='main_dir',
            field=models.CharField(default='Droite', choices=[('g', 'Gauche'), ('d', 'Droite')], max_length=1),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='medailles',
            field=models.CharField(default='Non applicable/Aucune', max_length=3000),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='mois_de_naissance',
            field=fiches.functions.IntegerRangeField(default='1'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='pj',
            field=models.CharField(default='Personnage joué', choices=[('p', 'Personnage joué'), ('a', 'Personnage jouable'), ('n', 'Personnage non joué')], max_length=1),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='poids',
            field=models.FloatField(default='70'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='profession',
            field=models.CharField(default='Prostipute', max_length=75),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='pseudo_du_personnage',
            field=models.CharField(default='?', max_length=30),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='race',
            field=models.CharField(default='Humaine', max_length=40),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='relations',
            field=models.CharField(default='Aucune', max_length=6000),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='sexe',
            field=models.CharField(default='Homme', choices=[('h', 'Homme'), ('f', 'Femme')], max_length=1),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='signes_dis',
            field=models.CharField(default='Aucun', max_length=200),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='taille',
            field=models.FloatField(default='1.70'),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='titre',
            field=models.CharField(default='Aucun', max_length=75),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='ville_de_naissance',
            field=models.CharField(default='Inconnue', max_length=50),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='ville_de_residence',
            field=models.CharField(default='Châtellerie', max_length=50),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='zone_de_naissance',
            field=models.SmallIntegerField(null=True, default=23, choices=[("Royaumes de l'est", ((600, 'Bois de la Pénombre'), (601, 'Bois des Chants éternels'), (602, 'Cap Strangleronce'), (603, 'Clairières de Tirisfal'), (604, 'Contreforts de Hautebrande'), (605, 'Dun Morogh'), (606, 'Défilé de Deuillevent'), (607, "Forêt d'Elwynn"), (608, 'Forêt des Pins-Argentés'), (609, 'Gilnéas'), (610, 'Gorge des Vents brûlants'), (611, 'Hautes-terres Arathies'), (612, 'Hautes-terres du Crépuscule'), (613, "Kul'Tiras"), (614, 'Les Carmines'), (615, 'Les Hinterlands'), (616, 'Les Paluns'), (617, 'Les terres Fantômes'), (618, 'Loch Modan'), (619, "Maleterres de l'Est"), (620, "Maleterres de l'Ouest"), (621, 'Marais des Chagrins'), (622, "Marche de l'Ouest"), (623, 'Noirebois'), (624, 'Steppes Ardentes'), (625, 'Strangleronce septentrionale'), (626, 'Terres Foudroyées'), (627, 'Terres Ingrates'), (628, "Île de Quel'Danas"))), ('Kalimdor', ((600, 'Azshara'), (601, "Berceau-de-l'Hiver"), (602, "Cratère d'Un'Goro"), (603, 'Durotar'), (604, 'Désolace'), (605, 'Féralas'), (606, 'Gangrebois'), (607, 'Les Serres-Rocheuses'), (608, "Marécage d'Âprefange"), (609, 'Mille pointes'), (610, 'Mont Hyjal'), (611, 'Mulgore'), (612, 'Orneval'), (613, 'Reflet-de-Lune'), (614, 'Silithus'), (615, 'Sombrivage'), (616, 'Tanaris'), (617, 'Tarides du Nord'), (618, 'Tarides du Sud'), (619, 'Teldrassil'), (620, 'Uldum'), (621, "Îles de l'Écho"))), ('Norfendre', ((600, 'Bassin de Sholazar'), (601, 'Désolation des dragons'), (602, 'Fjord Hurlant'), (603, 'Forêt du Chant de cristal'), (604, "Joug-d'hiver"), (605, 'La Couronne de glace'), (606, 'Les Grisonnes'), (607, 'Les pics Foudroyés'), (608, 'Toundra Boréenne'), (609, "Zul'Drak"))), ('Pandarie', ((600, 'Désert de Tanlong'), (601, 'Etendues sauvages de Krasarang'), (602, 'La forêt de Jade'), (603, 'Sommet de Kun-Lai'), (604, "Terres de l'Angoisse"), (605, "Val de l'Eternel Printemps"), (606, 'Vallée des Quatre vents'))), ('Iles brisées', ((600, 'Azsuna'), (601, 'Haut-Roc'), (602, 'Suramar'), (603, 'Tornheim'), (604, "Val'Sharah"))), ('Kezan', ((600, 'Kezan'),)), ('Zandalar', ((600, 'Zandalar'),))]),
        ),
        migrations.AlterField(
            model_name='fiche',
            name='zone_de_residence',
            field=models.SmallIntegerField(null=True, default=23, choices=[("Royaumes de l'est", ()), ('Kalimdor', ()), ('Norfendre', ()), ('Pandarie', ()), ('Iles brisées', ()), ('Kezan', ()), ('Zandalar', ())]),
        ),
        migrations.AlterField(
            model_name='inventaire',
            name='nom',
            field=models.CharField(default='Inventaire ', max_length=50),
        ),
        migrations.AlterField(
            model_name='objet',
            name='description',
            field=models.CharField(default='Aucune', max_length=500),
        ),
        migrations.AlterField(
            model_name='objet',
            name='image',
            field=models.ImageField(upload_to='images/users', default='images/site/WoWUnknownItem01.PNG'),
        ),
        migrations.AlterField(
            model_name='objet',
            name='qualite',
            field=models.CharField(default='Commun', choices=[('m', 'Médiocre'), ('c', 'Commun'), ('i', 'Inhabituel'), ('r', 'Rare'), ('e', 'Epique'), ('l', 'Légendaire'), ('u', 'Unique')], max_length=1),
        ),
        migrations.AlterField(
            model_name='quete',
            name='cible',
            field=models.CharField(default='Aucune', max_length=75),
        ),
        migrations.AlterField(
            model_name='quete',
            name='difficulte',
            field=models.SmallIntegerField(default=2, choices=[(1, 'Facile'), (2, 'Moyenne'), (3, 'Difficile'), (4, 'Très difficile'), (5, 'Suicidaire'), (6, 'Inconnue')]),
        ),
        migrations.AlterField(
            model_name='quete',
            name='ennemi',
            field=models.ImageField(upload_to='images/site/quest/ennemis', default='images/site/quest/Portraits/FollowerPortrait_NoPortrait.png'),
        ),
        migrations.AlterField(
            model_name='quete',
            name='etat',
            field=models.SmallIntegerField(default=1, choices=[(1, 'En attente'), (2, 'Réservée'), (3, 'Accomplie')]),
        ),
        migrations.AlterField(
            model_name='quete',
            name='recompense',
            field=models.CharField(default='Aucune', max_length=100),
        ),
        migrations.AlterField(
            model_name='quete',
            name='requis',
            field=models.CharField(default='Rien', max_length=100),
        ),
        migrations.AlterField(
            model_name='quete',
            name='zone',
            field=models.SmallIntegerField(null=True, default=23, choices=[("Royaumes de l'est", ()), ('Kalimdor', ()), ('Norfendre', ()), ('Pandarie', ()), ('Iles brisées', ()), ('Kezan', ()), ('Zandalar', ())]),
        ),
        migrations.AlterField(
            model_name='sorcier',
            name='bouclier_feu',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='sorcier',
            name='bouclier_mana',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='sorcier',
            name='grand_sorcier',
            field=models.BooleanField(default=False, choices=[(True, 'Oui'), (False, 'Non')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='images/users', default='images/site/no-image.png'),
        ),
    ]
