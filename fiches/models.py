# coding=utf-8
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from fiches.functions import IntegerRangeField


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

VIVANT = 'VI'
MORT = 'MO'
DISPARU = 'DI'
ETAT_CHOIX = (
    (VIVANT, 'Vivant'),
    (MORT, 'Mort'),
    (DISPARU, 'Disparu'),
)

MEMBRES = [
    (1, 'Main principale'),
    (2, 'Autre main'),
    (3, 'Tête'),
    (4, 'Epaules'),
    (5, 'Torse'),
    (6, 'Mains'),
    (7, 'Taille'),
    (8, 'Jambes'),
    (9, 'Pieds'),
    (10, 'Dos'),
    (11, 'Cou'),
    (12, 'Doigt'),
    (13, 'Poignets'),
    (14, 'Divers'),
    (15, 'Arme de secours')
    ]

ZONES = (
    ("Royaumes de l'est", (
        ("Bois de la Pénombre"),
        ("Bois des Chants éternels"),
        ("Cap Strangleronce"),
        ("Clairières de Tirisfal"),
        ("Contreforts de Hautebrande"),
        ("Dun Morogh"),
        ("Défilé de Deuillevent"),
        ("Forêt d'Elwynn"),
        ("Forêt des Pins-Argentés"),
        ("Gilnéas"),
        ("Gorge des Vents brûlants"),
        ("Hautes-terres Arathies"),
        ("Hautes-terres du Crépuscule"),
        ("Kul'Tiras"),
        ("Les Carmines"),
        ("Les Hinterlands"),
        ("Les Paluns"),
        ("Les terres Fantômes"),
        ("Loch Modan"),
        ("Maleterres de l'Est"),
        ("Maleterres de l'Ouest"),
        ("Marais des Chagrins"),
        ("Marche de l'Ouest"),
        ("Noirebois"),
        ("Steppes Ardentes"),
        ("Strangleronce septentrionale"),
        ("Terres Foudroyées"),
        ("Terres Ingrates"),
        ("Île de Quel'Danas"),
    )
    ),
    ("Kalimdor", (
        ("Azshara"),
        ("Berceau-de-l'Hiver"),
        ("Cratère d'Un'Goro"),
        ("Durotar"),
        ("Désolace"),
        ("Féralas"),
        ("Gangrebois"),
        ("Les Serres-Rocheuses"),
        ("Marécage d'Âprefange"),
        ("Mille pointes"),
        ("Mont Hyjal"),
        ("Mulgore"),
        ("Orneval"),
        ("Reflet-de-Lune"),
        ("Silithus"),
        ("Sombrivage"),
        ("Tanaris"),
        ("Tarides du Nord"),
        ("Tarides du Sud"),
        ("Teldrassil"),
        ("Uldum"),
        ("Îles de l'Écho"),
    )
    ),
    ("Norfendre", (
        ("Bassin de Sholazar"),
        ("Désolation des dragons"),
        ("Fjord Hurlant"),
        ("Forêt du Chant de cristal"),
        ("Joug-d'hiver"),
        ("La Couronne de glace"),
        ("Les Grisonnes"),
        ("Les pics Foudroyés"),
        ("Toundra Boréenne"),
        ("Zul'Drak")
    )
    ),
    ("Pandarie", (
        ("Désert de Tanlong"),
        ("Etendues sauvages de Krasarang"),
        ("La forêt de Jade"),
        ("Sommet de Kun-Lai"),
        ("Terres de l'Angoisse"),
        ("Val de l'Eternel Printemps"),
        ("Vallée des Quatre vents")
    )
    ),
    ("Iles brisées", (
        ("Azsuna"),
        ("Haut-Roc"),
        ("Suramar"),
        ("Tornheim"),
        ("Val'Sharah")
    )
    ),
    ("Kezan", (
        ("Kezan"),
    )
    ),
    ("Zandalar", (
        ("Zandalar"),
    )
    )
)

# Construct the actual ZONES_CHOIX tuple
ZONES_CHOIX = []
for (ri, (region, zones)) in zip(range(len(ZONES)), ZONES):
    nums = range(len(zones))
    nums = map(lambda n: ri * 100 + n, nums)
    ZONES_CHOIX.append((region, list(zip(nums, zones))))


class Fiche(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    autres_prenoms = models.CharField(max_length=200,
                                      default='Aucun')
    ne = models.CharField(max_length=50,
                          default='Non applicable')
    titre = models.CharField(max_length=75,
                             default='Aucun')
    autres_titres = models.CharField(max_length=500,
                                     default='Aucun')
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Homme"),
                                ('f', "Femme")
                            )),
                            default="h")
    race = models.CharField(max_length=40,
                            default='Humaine')
    taille = models.FloatField(default='1.70')
    poids = models.FloatField(default='70')
    c_yeux = models.CharField(max_length=30,
                              default='Marron')
    c_cheveux = models.CharField(max_length=30,
                                 default='Brun')
    signes_dis = models.CharField(max_length=200,
                                  default='Aucun')
    profession = models.CharField(max_length=75,
                                  default='Prostipute')
    medailles = models.CharField(max_length=3000,
                                 default='Non applicable/Aucune')
    etat = models.CharField(max_length=2,
                            choices=ETAT_CHOIX,
                            default=VIVANT)
    pj = models.CharField(max_length=1,
                          choices=((
                              ('p', "Personnage joué"),
                              ('a', "Personnage jouable"),
                              ('n', "Personnage non joué")
                          )),
                          default="p")
    jour_de_naissance = IntegerRangeField(default='1', min_value=1,
                                          max_value=31)
    mois_de_naissance = IntegerRangeField(default='1', min_value=1,
                                          max_value=12)
    annee_de_naissance = IntegerRangeField(default='0', min_value=-32000,
                                           max_value=100)
    zone_de_naissance = models.SmallIntegerField(choices=ZONES_CHOIX,
                                                 default=23,
                                                 null=True)
    ville_de_naissance = models.CharField(max_length=50,
                                          default='Inconnue')
    zone_de_residence = models.SmallIntegerField(choices=ZONES_CHOIX,
                                                 default=23,
                                                 null=True)
    ville_de_residence = models.CharField(max_length=50,
                                          default='Châtellerie')
    description = models.CharField(max_length=6000,
                                   default='A venir')
    historique = models.CharField(max_length=6000,
                                  default='A venir')
    inventaire = models.CharField(max_length=6000,
                                  null=True,
                                  blank=True,
                                  default='A venir')
    relations = models.CharField(max_length=6000,
                                 default='Aucune')
    competences = models.CharField(max_length=6000,
                                   default='Aucune')
    image = models.ImageField(upload_to='images/persos',
                              default='images/site/no-image.png')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='fiches')
    pseudo_du_personnage = models.CharField(max_length=30,
                                            default="?")
    main_dir = models.CharField(max_length=1,
                                choices=((
                                    ('g', "Gauche"),
                                    ('d', "Droite")
                                )),
                                default="d")
    afficher_createur = models.BooleanField(default=True,
                                            choices=(
                                                (True, 'Oui'),
                                                (False, 'Non'),
                                            ))
    afficher_inventaire = models.BooleanField(default=True,
                                              choices=(
                                                  (True, 'Oui'),
                                                  (False, 'Non'),
                                              ))
    afficher_pseudo = models.BooleanField(default=True,
                                          choices=(
                                              (True, 'Oui'),
                                              (False, 'Non'),
                                          ))
    creation = models.DateField(default=timezone.now)
    inventaire_fdg = models.OneToOneField('Inventaire',
                                          blank=True,
                                          null=True,
                                          related_name='proprietaire')
    equipement = models.OneToOneField('Equipement',
                                      blank=True,
                                      null=True,
                                      related_name='proprietaire')

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "fiche"
        verbose_name_plural = "fiches"
        default_related_name = 'fiches'
        permissions = (("plus_de_15_fiches",
                        "Peut faire plus de quinze fiches"),)

    def __unicode__(self):
        return u'%s %s' % (self.nom, self.prenom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True,
                                related_name='infos')
    image = models.ImageField(upload_to='images/users',
                              default='images/site/no-image.png')
    naissance = models.DateField()
    affichage_date = models.CharField(max_length=1,
                                      choices=((
                                          ('n', "Normal"),
                                          ('l', "Long")
                                      )),
                                      default="l")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% OBJETS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Objet(models.Model):
    nom = models.CharField(max_length=75)
    qualite = models.CharField(max_length=1,
                               choices=((
                                   ('m', "Médiocre"),
                                   ('c', "Commun"),
                                   ('i', "Inhabituel"),
                                   ('r', "Rare"),
                                   ('e', "Epique"),
                                   ('l', "Légendaire"),
                                   ('u', "Unique")
                               )),
                               default="c")
    description = models.CharField(max_length=500,
                                   default='Aucune')
    prix = models.IntegerField(default=0)
    poids = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='images/objets',
    #                           default='images/site/WoWUnknownItem01.PNG')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='objet')
    image_url = models.CharField(max_length=50,
                                 default='WoWUnknownItem01')

    class Meta:
        ordering = ["nom"]
        verbose_name = "objet"
        verbose_name_plural = "objets"
        default_related_name = 'objet'
        permissions = (("objet_ok",
                        "Peut faire des objets"),)

    def has_equipement(self):
        return hasattr(self, 'armure')

    def __unicode__(self):
        return u'%s' % (self.nom)


class Armure(models.Model):
    objet = models.OneToOneField(Objet,
                                 null=True,
                                 related_name='armure')
    effet = models.CharField(max_length=400,
                             default='Aucun')
    effet_ig = models.CharField(max_length=400,
                                default='Aucun')
    force = IntegerRangeField(default=0, min_value=0,
                              max_value=25)
    intell = IntegerRangeField(default=0, min_value=0,
                               max_value=25)
    agi = IntegerRangeField(default=0, min_value=0,
                            max_value=25)
    membre = models.SmallIntegerField(choices=MEMBRES,
                                      default=5)
    armure = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["membre"]
        verbose_name = "armure"
        verbose_name_plural = "armures"
        default_related_name = 'armure'
        permissions = (("armure_ok",
                        "Peut faire des armures"),)

    def get_nom(self):
        return self.objet.nom


class Case(models.Model):
    nombre = IntegerRangeField(default=1, min_value=0,
                               max_value=99)
    objet = models.ForeignKey(Objet,
                              null=True,
                              related_name='case')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='cases')

    class Meta:
        ordering = ["nombre", "objet"]
        verbose_name = "case"
        verbose_name_plural = "cases"
        default_related_name = 'case'
        permissions = (("case_ok",
                        "Peut faire des cases"),)

    def get_nom(self):
        return (str(self.nombre) + " " + self.objet.nom)


class Inventaire(models.Model):
    nom = models.CharField(max_length=50,
                           default="Inventaire ")
    cases = models.ManyToManyField(Case,
                                   related_name='inventaire')

    class Meta:
        verbose_name = "inventaire"
        verbose_name_plural = "inventaires"
        default_related_name = 'inventaire'
        permissions = (("inventaire_ok",
                        "Peut faire des inventaires"),)

    def __unicode__(self):
        return u'%s' % (self.nom)


class Equipement(models.Model):
    nom = models.CharField(max_length=50,
                           default="Equipement ")
    objets = models.ManyToManyField(Armure,
                                    related_name='equipement')

    class Meta:
        verbose_name = "equipement"
        verbose_name_plural = "equipements"
        default_related_name = 'equipement'
        permissions = (("equipement_ok",
                        "Peut faire des équipements"),)

    def get_mp(self):
        return self.objets.filter(membre=1).first()

    def get_am(self):
        return self.objets.filter(membre=2).first()

    def get_tete(self):
        return self.objets.filter(membre=3).first()

    def get_epaules(self):
        return self.objets.filter(membre=4).first()

    def get_torse(self):
        return self.objets.filter(membre=5).first()

    def get_mains(self):
        return self.objets.filter(membre=6).first()

    def get_taille(self):
        return self.objets.filter(membre=7).first()

    def get_jambes(self):
        return self.objets.filter(membre=8).first()

    def get_pieds(self):
        return self.objets.filter(membre=9).first()

    def get_dos(self):
        return self.objets.filter(membre=10).first()

    def get_cou(self):
        return self.objets.filter(membre=11).first()

    def get_doigts(self):
        ret = list(self.objets.filter(membre=12)[:8].iterator())
        ret += [None] * (8 - len(ret))
        return ret

    def get_poignets(self):
        return self.objets.filter(membre=13).first()

    def get_divers(self):
        ret = list(self.objets.filter(membre=14)[:10].iterator())
        ret += [None] * (8 - len(ret))
        return ret

    def get_autre_arme(self):
        return self.objets.filter(membre=15).first()

    def effets(self):
        effets = []
        effets_ig = []
        force = 0
        intell = 0
        agi = 0
        armure = 0
        run_compte = 0
        runique = False
        ter_compte = 0
        terradiance = False
        methods = [self.get_mp, self.get_am, self.get_tete, self.get_epaules,
                   self.get_torse, self.get_mains, self.get_taille,
                   self.get_jambes, self.get_pieds, self.get_dos, self.get_cou,
                   self.get_poignets, self.get_autre_arme]
        for method in methods:
            objet = method()
            if objet is not None:
                effets.append("De \"" + objet.objet.nom + "\" : " + objet.effet)
                effets_ig.append("De \"" + objet.objet.nom + "\" : " + objet.effet_ig)
                m = objet.membre
                if (m >= 3 and m <=9) or m == 13:
                    if ("runique" in objet.objet.nom):
                        run_compte += 1
                    if ("terradiance" in objet.objet.nom):
                        ter_compte += 1
                force += objet.force
                intell += objet.intell
                agi += objet.agi
                armure += objet.armure
        for anneau in self.get_doigts():
            if anneau is not None:
                effets.append("De \"" + anneau.objet.nom + "\" : " + anneau.effet)
                effets_ig.append("De \"" + anneau.objet.nom + "\" : " + anneau.effet_ig)
                force += anneau.force
                intell += anneau.intell
                agi += anneau.agi
                armure += anneau.armure
        for diver in self.get_divers():
            if diver is not None:
                effets.append("De \"" + diver.objet.nom + "\" : " + diver.effet)
                effets_ig.append("De \"" + diver.objet.nom + "\" : " + diver.effet_ig)
                force += diver.force
                intell += diver.intell
                agi += diver.agi
                armure += diver.armure
        if ter_compte == 8:
            terradiance = True
        if run_compte == 8:
            run_compte = True
        return effets, effets_ig, force, intell, agi, armure, runique, terradiance

    def __unicode__(self):
        return u'%s' % (self.nom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUETES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Quete(models.Model):
    nom = models.CharField(max_length=75)
    objectif = models.CharField(max_length=600)
    cible = models.CharField(max_length=75,
                             default='Aucune')
    requis = models.CharField(max_length=100,
                              default='Rien')
    zone = models.SmallIntegerField(choices=ZONES_CHOIX,
                                    default=23,
                                    null=True)
    localisation = models.CharField(max_length=75)
    x = models.SmallIntegerField(default=0)
    y = models.SmallIntegerField(default=0)
    nb_combattants = models.SmallIntegerField(default=1)
    difficulte = models.SmallIntegerField(choices=((
        (1, "Facile"),
        (2, "Moyenne"),
        (3, "Difficile"),
        (4, "Très difficile"),
        (5, "Suicidaire"),
        (6, "Inconnue")
    )),
                                          default=2)
    recompense = models.CharField(max_length=100,
                                  default='Aucune')
    gloire = models.SmallIntegerField(default=0)
    etat = models.SmallIntegerField(choices=((
        (1, "En attente"),
        (2, "Réservée"),
        (3, "Accomplie")
    )),
                                    default=1)
    reservee = models.ForeignKey(Fiche,
                                 blank=True,
                                 null=True,
                                 related_name='quete_reservee')
    leader = models.ForeignKey(Fiche,
                               null=True,
                               blank=True,
                               related_name='quete_reussie')
    ennemi = models.CharField(max_length=60,
                              default='images/site/quest/Portraits/FollowerPortrait_NoPortrait.png')
    creation = models.DateField(default=timezone.now)

    class Meta:
        ordering = ["nom", "difficulte"]
        verbose_name = "quête"
        verbose_name_plural = "quêtes"
        default_related_name = 'quete'
        permissions = (("quete_ok",
                        "Peut prendre des quêtes"),)

    def __unicode__(self):
        return u'%s' % (self.nom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RAPPORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Operation(models.Model):
    nom = models.CharField(max_length=100)
    dirigeant = models.ForeignKey(Fiche,
                                  null=True,
                                  blank=True,
                                  related_name='dirigeant_op')

    class Meta:
        ordering = ["nom"]
        verbose_name = "opération"
        verbose_name_plural = "opérations"
        default_related_name = 'opération'

    def __unicode__(self):
        return u'%s' % (self.nom)


class Mission(models.Model):
    operation = models.ForeignKey(Operation,
                                  null=True,
                                  blank=True,
                                  related_name='mission')
    dirigeant = models.ForeignKey(Fiche,
                                  null=True,
                                  blank=True,
                                  related_name='dirigeant_mission')
    autre_dirigeant = models.ForeignKey(Fiche,
                                        null=True,
                                        blank=True,
                                        related_name='autre_dirigeant')
    numero = models.SmallIntegerField(default=0)
    lieu = models.CharField(max_length=100)
    jour = IntegerRangeField(default='1', min_value=1,
                             max_value=31)
    mois = IntegerRangeField(default='1', min_value=1,
                             max_value=12)
    annee = IntegerRangeField(default='0', min_value=0,
                              max_value=100)
    type_mis = models.SmallIntegerField(choices=[
        (1, 'Embuscade'),
        (2, 'Assaut'),
        (3, 'Siège'),
        (4, 'Défense'),
        (5, 'Escorte'),
        (6, 'Voyage'),
        (7, 'Prendre et tenir'),
        (8, 'Escarmouche'),
        (9, 'Bataille rangée'),
        (10, 'Rechercher et détruire'),
        (11, 'Sabotage'),
        (12, 'Infiltration'),
        (13, 'Espionnage'),
        (14, 'Sauvetage'),
        (15, 'Récupération'),
        (16, 'Assassinat'),
        (17, 'Incident')
    ],
                                        default=8)
    objectif = models.CharField(max_length=300)
    participants = models.CharField(max_length=500)
    deroulement = models.CharField(max_length=6000)
    signature_url = models.CharField(max_length=100,
                                     default="c: L. Vaanes")

    class Meta:
        ordering = ["numero"]
        verbose_name = "mission"
        verbose_name_plural = "missions"
        default_related_name = 'mission'

    def __unicode__(self):
        return u'%s' % (self.operation.nom + " : " + self.lieu + ", le " + str(self.jour) + "." + str(self.mois) + "." + str(self.annee))
