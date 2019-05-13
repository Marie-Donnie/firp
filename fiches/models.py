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
    ),
    ("Mers", (
        ("Mer Interdite"),
        ("Mer Voilée"),
        ("Mer Gelée"),
        ("Grande Mer")
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
    signes_dis = models.CharField(max_length=600,
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
    autres_informations = models.CharField(max_length=600,
                                           default='Aucune')
    image = models.ImageField(upload_to='images/persos',
                              default='images/site/no-image.png')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='fiches',
                                 on_delete=models.CASCADE)
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
    afficher_bourse = models.BooleanField(default=True,
                                          choices=(
                                              (True, 'Oui'),
                                              (False, 'Non'),
                                          ))
    creation = models.DateField(default=timezone.now)
    inventaire_fdg = models.OneToOneField('Inventaire',
                                          blank=True,
                                          null=True,
                                          related_name='proprietaire',
                                          on_delete=models.SET_NULL)
    equipement = models.OneToOneField('Equipement',
                                      blank=True,
                                      null=True,
                                      related_name='proprietaire',
                                      on_delete=models.SET_NULL)
    bourse = models.OneToOneField('Bourse',
                                  blank=True,
                                  null=True,
                                  related_name='proprietaire',
                                  on_delete=models.SET_NULL)

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "fiche"
        verbose_name_plural = "fiches"
        default_related_name = 'fiches'
        permissions = (("plus_de_15_fiches",
                        "Peut faire plus de quinze fiches"),
                       ("fdg",
                       "Est fils de Garithos"),
                       ("veteran",
                        "FdG + accès à plus de fonctionnalités."),
                       ("admin",
                        "Est admin"),
                       ("allie",
                        "Est allié"),
                       ("chef",
                        "Est chef"),)

    def __unicode__(self):
        return u'%s %s' % (self.nom, self.prenom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True,
                                related_name='infos',
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/users',
                              default='images/site/no-image.png')
    naissance = models.DateField(blank=True,
                                 null=True,)
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
                                 related_name='objet',
                                 on_delete=models.SET_NULL)
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
                                 related_name='armure',
                                 on_delete=models.CASCADE)
    effet = models.CharField(max_length=400,
                             default='Aucun')
    effet_ig = models.CharField(max_length=400,
                                default='Aucun')
    force = IntegerRangeField(default=0, min_value=0,
                              max_value=25)
    intell = IntegerRangeField(default=0, min_value=0,
                               max_value=200)
    agi = IntegerRangeField(default=0, min_value=0,
                            max_value=25)
    membre = models.SmallIntegerField(choices=MEMBRES,
                                      default=5)
    armure = models.FloatField(default=0)

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
                              related_name='case',
                              on_delete=models.CASCADE)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='cases',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ["objet", "nombre"]
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
                                    blank=True,
                                    related_name='equipement')
    enchantements = models.ManyToManyField('Enchantement',
                                           blank=True,
                                           related_name='equipement')

    class Meta:
        verbose_name = "equipement"
        verbose_name_plural = "equipements"
        default_related_name = 'equipement'
        permissions = (("equipement_ok",
                        "Peut faire des équipements"),)

    def get_mp(self):
        return self.objets.filter(membre=1).first(), self.enchantements.filter(membre=1).first()

    def get_am(self):
        return self.objets.filter(membre=2).first(), self.enchantements.filter(membre=2).first()

    def get_tete(self):
        return self.objets.filter(membre=3).first(), self.enchantements.filter(membre=3).first()

    def get_epaules(self):
        return self.objets.filter(membre=4).first(), self.enchantements.filter(membre=4).first()

    def get_torse(self):
        return self.objets.filter(membre=5).first(), self.enchantements.filter(membre=5).first()

    def get_mains(self):
        return self.objets.filter(membre=6).first(), self.enchantements.filter(membre=6).first()

    def get_taille(self):
        return self.objets.filter(membre=7).first(), self.enchantements.filter(membre=7).first()

    def get_jambes(self):
        return self.objets.filter(membre=8).first(), self.enchantements.filter(membre=8).first()

    def get_pieds(self):
        return self.objets.filter(membre=9).first(), self.enchantements.filter(membre=9).first()

    def get_dos(self):
        return self.objets.filter(membre=10).first(), self.enchantements.filter(membre=10).first()

    def get_cou(self):
        return self.objets.filter(membre=11).first(), self.enchantements.filter(membre=11).first()

    def get_doigts(self):
        ret = list(self.objets.filter(membre=12)[:8].iterator())
        ret += [None] * (8 - len(ret))
        return ret

    def get_poignets(self):
        return self.objets.filter(membre=13).first(), self.enchantements.filter(membre=13).first()

    def get_divers(self):
        ret = list(self.objets.filter(membre=14)[:10].iterator())
        ret += [None] * (8 - len(ret))
        return ret

    def get_autre_arme(self):
        return self.objets.filter(membre=15).first(), self.enchantements.filter(membre=15).first()

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
            objet, enchantement = method()
            if objet is not None:
                effets.append("\"" + objet.objet.nom + "\" : " + objet.effet)
                effets_ig.append("\"" + objet.objet.nom + "\" : " + objet.effet_ig)
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
                if enchantement is not None:
                    effets.append("\"" + enchantement.nom + "\" : " + enchantement.effet)
                    effets_ig.append("\"" + enchantement.nom + "\" : " + enchantement.effet_ig)
                    force += enchantement.force
                    intell += enchantement.intell
                    agi += enchantement.agi
        for anneau in self.get_doigts():
            if anneau is not None:
                effets.append("\"" + anneau.objet.nom + "\" : " + anneau.effet)
                effets_ig.append("\"" + anneau.objet.nom + "\" : " + anneau.effet_ig)
                force += anneau.force
                intell += anneau.intell
                agi += anneau.agi
                armure += anneau.armure
        for diver in self.get_divers():
            if diver is not None:
                effets.append("\"" + diver.objet.nom + "\" : " + diver.effet)
                effets_ig.append("\"" + diver.objet.nom + "\" : " + diver.effet_ig)
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


class Enchantement(models.Model):
    nom = models.CharField(max_length=50,
                            default="Enchantement de ")
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
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='enchantement',
                                 on_delete=models.SET_NULL)

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
                                 related_name='quete_reservee',
                                 on_delete=models.SET_NULL)
    leader = models.ForeignKey(Fiche,
                               null=True,
                               blank=True,
                               related_name='quete_reussie',
                               on_delete=models.SET_NULL)
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
                                  related_name='dirigeant_op',
                                  on_delete=models.SET_NULL)

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
                                  related_name='mission',
                                  on_delete=models.SET_NULL)
    dirigeant = models.ForeignKey(Fiche,
                                  null=True,
                                  blank=True,
                                  related_name='dirigeant_mission',
                                  on_delete=models.SET_NULL)
    autre_dirigeant = models.ForeignKey(Fiche,
                                        null=True,
                                        blank=True,
                                        related_name='autre_dirigeant',
                                        on_delete=models.SET_NULL)
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
        (17, 'Incident'),
        (18, 'Reconnaissance'),
        (19, 'Opération clandestine')
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


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% SORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Classe(models.Model):
    nom = models.CharField(max_length=50)
    principes = models.CharField(max_length=1000)
    image_url = models.CharField(max_length=50,
                                 default='WoWUnknownItem01')
    fond_url = models.CharField(max_length=50,
                                 default='paladin')

    def __unicode__(self):
        return u'%s' % (self.nom)

class Sort(models.Model):
    nom = models.CharField(max_length=50)
    condition = models.CharField(max_length=75,
                                 null=True,
                                 blank=True,
                                 default='aucune')
    cout = models.CharField(max_length=50,
                            null=True,
                            blank=True)
    seuil = models.CharField(max_length=10,
                             null=True,
                             blank=True)
    duree_incant = models.CharField(max_length=50,
                                    null=True,
                                    blank=True)
    effet = models.CharField(max_length=400)
    duree_sort = models.CharField(max_length=50,
                                  null=True,
                                  blank=True)
    classe = models.ForeignKey(Classe,
                               null=True,
                               blank=True,
                               related_name='sort',
                               on_delete=models.SET_NULL)
    image_url = models.CharField(max_length=50,
                                 default='WoWUnknownItem01')

    def __unicode__(self):
        return u'%s' % (self.nom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Image(models.Model):
    nom = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/uploads')

    def __unicode__(self):
        return u'%s' % (self.nom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMERCES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Bourse(models.Model):
    nom = models.CharField(max_length=50,
                           default='')
    argent = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return u'%s' % (self.nom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% HABITATIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Piece(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=999)
    surface = models.SmallIntegerField(default=10)
    mobilier = models.CharField(max_length=500)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='piece',
                                 on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/maisons',
                              default='images/site/no-image.png')

    def __unicode__(self):
        return u'%s' % (self.nom)


class Etage(models.Model):
    nom = models.CharField(max_length=50,
                           default='Etage ')
    numero = models.SmallIntegerField(default=1)
    pieces = models.ManyToManyField(Piece,
                                    blank=True,
                                    related_name='etage')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='etage',
                                 on_delete=models.SET_NULL)

    def __unicode__(self):
        return u'%s' % (self.nom)


class Maison(models.Model):
    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=999)
    type_m = models.SmallIntegerField(choices=[
        (1, 'Taudis en bois'),
        (2, 'Cabane en bois'),
        (3, 'Chaumière'),
        (4, 'Maison modeste'),
        (5, 'Maison de pierre'),
        (6, 'Maison riche'),
        (7, 'Manoir'),
        (8, 'Chambre au château'),
        (9, 'Chambre au monastère')
    ],
                                        default=2)
    ville = models.CharField(max_length=50)
    rue = models.CharField(max_length=50)
    numero = models.SmallIntegerField(default=1)
    materiel_f = models.CharField(max_length=50)
    materiel_c = models.CharField(max_length=50)
    surface_etage = models.SmallIntegerField(default=30)
    nb_etage = models.SmallIntegerField(default=1)
    nb_habitants = models.SmallIntegerField(default=1)
    habitants = models.CharField(max_length=6000,
                                 default='Aucun')
    nb_serviteurs = models.SmallIntegerField(default=0)
    etages = models.ManyToManyField(Etage,
                                    blank=True,
                                    related_name='maison')
    com_ill = models.BooleanField(default=False,
                                  choices=(
                                      (True, 'Oui'),
                                      (False, 'Non'),
                                  ))
    type_commerce = models.CharField(max_length=50,
                                     blank=True,
                                     null=True)
    materiel = models.CharField(max_length=500,
                                     blank=True,
                                     null=True)
    prod = models.CharField(max_length=500,
                                     blank=True,
                                     null=True)
    rente = models.SmallIntegerField(default=0,
                                     blank=True,
                                     null=True)
    proprietaire = models.ForeignKey(Fiche,
                                     blank=True,
                                     null=True,
                                     related_name='maison',
                                     on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/maisons',
                              default='images/site/no-image.png')

    def __unicode__(self):
        return u'%s' % (self.nom)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONSEIL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #



# class Chef(models.Model):
#     createur = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                  null=True,
#                                  related_name='chef')
#     image = models.ImageField(upload_to='images/conseil',
#                               default='images/site/no-image.png')

#     class Meta:
#         permissions = (("chef_ok",
#                         "Est un chef"),)

class Legende(models.Model):
    nom = models.CharField(max_length=75,
                           default='Légende')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='legende',
                                 related_query_name='legende',
                                 on_delete=models.SET_NULL)
    description = models.CharField(max_length=6000,
                                   default='A venir')
    image = models.ImageField(upload_to='images/persos',
                              default='images/site/no-image.png')

    class Meta:
        verbose_name = "légende"
        verbose_name_plural = "légendes"
        default_related_name = 'légende'

    def __unicode__(self):
        return u'%s' % (self.nom)


class Token(models.Model):
    token = models.CharField(max_length=75,
                           null=True)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='token',
                                 related_query_name='token',
                                 on_delete=models.CASCADE)
