# coding=utf-8
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime


class IntegerRangeField(models.SmallIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.SmallIntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()


# Create your models here.

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
    (14, 'Divers')
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
    ZONES_CHOIX.append((region, zip(nums, zones)))


class Fiche(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    autres_prenoms = models.CharField(max_length=200,
                                      default='Aucun')
    titre = models.CharField(max_length=75,
                             default='Aucun')
    autres_titres = models.CharField(max_length=500,
                                     default='Aucun')
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Homme"),
                                ('f', "Femme")
                            )),
                            default="Homme")
    race = models.CharField(max_length=40,
                            default='Humaine')
    taille = models.FloatField(default='1.70')
    poids = models.FloatField(default='70')
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
                          default="Personnage joué")
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
                                default="Droite")
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
    rpg = models.ForeignKey('Rpg',
                            blank=True,
                            null=True)

    class Meta:
        ordering = ["nom", "prenom"]
        verbose_name = "fiche"
        verbose_name_plural = "fiches"
        default_related_name = 'fiches'
        permissions = (("plus_de_15_fiches",
                        "Peut faire plus de quinze fiches"),)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                null=True,
                                related_name='infos')
    image = models.ImageField(upload_to='images/users',
                              default='images/site/no-image.png')
    naissance = models.DateField()


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
                               default="Commun")
    description = models.CharField(max_length=500,
                                   default='Aucune')
    prix = models.IntegerField(default=0)
    poids = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/users',
                              default='images/site/WoWUnknownItem01.PNG')

    class Meta:
        ordering = ["nom"]
        verbose_name = "objet"
        verbose_name_plural = "objets"
        default_related_name = 'objet'
        permissions = (("objet_ok",
                        "Peut faire des objets"),)

    def has_equipement(self):
        return hasattr(self, 'armure')


class Armure(models.Model):
    objet = models.OneToOneField(Objet,
                                 null=True,
                                 related_name='armure')
    effet = models.CharField(max_length=100,
                             default='Aucun')
    autres_effets = models.CharField(max_length=100,
                                     default='Aucun')
    effet_ig = models.CharField(max_length=100,
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
                           default="Inventaire")
    cases = models.ManyToManyField(Case,
                                   related_name='inventaire')

    class Meta:
        verbose_name = "inventaire"
        verbose_name_plural = "inventaires"
        default_related_name = 'inventaire'
        permissions = (("inventaire_ok",
                        "Peut faire des inventaires"),)


class Equipement(models.Model):
    nom = models.CharField(max_length=50,
                           default="Equipement")
    objets = models.ManyToManyField(Armure,
                                    related_name='equipement')

    class Meta:
        verbose_name = "equipement"
        verbose_name_plural = "equipements"
        default_related_name = 'equipement'
        permissions = (("equipement_ok",
                        "Peut faire des équipements"),)

    def get_mp(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 1:
                ret.append(i)
        return ret[0] if ret else ret

    def get_am(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 2:
                ret.append(i)
        return ret[0] if ret else ret

    def get_tete(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 3:
                ret.append(i)
        return ret[0] if ret else ret

    def get_epaules(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 4:
                ret.append(i)
        return ret[0] if ret else ret

    def get_torse(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 5:
                ret.append(i)
        return ret[0] if ret else ret

    def get_mains(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 6:
                ret.append(i)
        return ret[0] if ret else ret

    def get_taille(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 7:
                ret.append(i)
        return ret[0] if ret else ret

    def get_jambes(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 8:
                ret.append(i)
        return ret[0] if ret else ret

    def get_pieds(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 9:
                ret.append(i)
        return ret[0] if ret else ret

    def get_dos(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 10:
                ret.append(i)
        return ret[0] if ret else ret

    def get_cou(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 11:
                ret.append(i)
        return ret[0] if ret else ret

    def get_doigts(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 12:
                ret.append(i)
        if ret.length < 8:
            for x in xrange(8 - ret.length):
                ret.append(None)
        return ret

    def get_poignets(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 13:
                ret.append(i)
        return ret[0] if ret else ret

    def get_divers(self):
        ret = []
        for i in self.objets.all():
            if i.membre == 14:
                ret.append(i)
        if ret.length < 10:
            for x in xrange(10 - ret.length):
                ret.append(None)
        return ret

    # def get_equipement(self):
    #     return self.get_mp() + self.get_am() + self.get_tete() + self.get_epaules() + self.get_torse() + self.get_mains() + self.get_taille() + self.get_jambes() + self.get_pieds() + self.get_dos() + self.get_cou() + self.get_doigts() + self.get_poignets() + self.get_divers()


class Rpg(models.Model):
    nom = models.CharField(max_length=50,
                           default="Classique")

    class Meta:
        verbose_name = "rpg"
        verbose_name_plural = "rpgs"
        default_related_name = 'rpg'
        permissions = (("plusieurs_rpgs",
                        "Participe à d'autres campagnes"),)


class Avant_garde(Rpg):
    race_rpg = models.CharField(max_length=1,
                                choices=((
                                    ('n', "Nain"),
                                    ('e', "Haut-elfe"),
                                    ('h', "Humain")
                                )),
                                default="Humain")
    ex_prof = models.SmallIntegerField(choices=((
        (1, "Forgeron"),
        (2, "Chasseur"),
        (3, "Cuisinier"),
        (4, "Tavernier"),
        (5, "Facteur d'arc"),
        (6, "Tanneur"),
        (7, "Architecte"),
        (8, "Ebéniste"),
        (9, "Autre métier")
    )),
                                       default=9)
    cap_combat = IntegerRangeField(default=1, min_value=1,
                                   max_value=10)
    cap_tir = IntegerRangeField(default=1, min_value=1,
                                max_value=10)
    force = IntegerRangeField(default=1, min_value=1,
                              max_value=10)
    endu = IntegerRangeField(default=1, min_value=1,
                             max_value=10)
    perce = IntegerRangeField(default=1, min_value=1,
                              max_value=10)
    agi = IntegerRangeField(default=1, min_value=1,
                            max_value=10)
    intell = IntegerRangeField(default=1, min_value=1,
                               max_value=10)
    charisme = IntegerRangeField(default=1, min_value=1,
                                 max_value=10)
    force_men = IntegerRangeField(default=1, min_value=1,
                                  max_value=10)
    pv = models.SmallIntegerField(default=11)
    ps = models.SmallIntegerField(default=0)
    pf = models.SmallIntegerField(default=0)
    niveau = models.SmallIntegerField(default=1)
    xp = models.SmallIntegerField(default=0)
    blessures = models.CharField(max_length=800,
                                 null=True,
                                 blank=True,
                                 default='Sans')
    troubles_ment = models.CharField(max_length=800,
                                     null=True,
                                     blank=True,
                                     default='Sans')
    classe = models.ForeignKey('Classe_ag',
                               blank=True,
                               null=True)


class Classe_ag(models.Model):
    nom = models.CharField(max_length=50,
                           default="Fantassin")


class Fantassin(Classe_ag):
    intim = IntegerRangeField(default=0, min_value=1,
                              max_value=100)
    parer_fleches = IntegerRangeField(default=0, min_value=1,
                                      max_value=100)
    athle = models.BooleanField(default=False,
                                choices=(
                                    (True, 'Oui'),
                                    (False, 'Non'),
                                ))
    resistant = models.BooleanField(default=False,
                                    choices=(
                                        (True, 'Oui'),
                                        (False, 'Non'),
                                    ))
    cc = IntegerRangeField(default=0, min_value=1,
                           max_value=100)
    prot = IntegerRangeField(default=0, min_value=1,
                             max_value=100)
    epeiste = models.BooleanField(default=False,
                                  choices=(
                                      (True, 'Oui'),
                                      (False, 'Non'),
                                  ))
    crane_dur = models.BooleanField(default=False,
                                    choices=(
                                        (True, 'Oui'),
                                        (False, 'Non'),
                                    ))
    equitation = IntegerRangeField(default=0, min_value=1,
                                   max_value=100)
    maitr_glaive = models.BooleanField(default=False,
                                       choices=(
                                           (True, 'Oui'),
                                           (False, 'Non'),
                                       ))
    maitr_arm_lourde = models.BooleanField(default=False,
                                           choices=(
                                               (True, 'Oui'),
                                               (False, 'Non'),
                                           ))
    feroce = models.BooleanField(default=False,
                                 choices=(
                                     (True, 'Oui'),
                                     (False, 'Non'),
                                 ))
    implacable = models.BooleanField(default=False,
                                     choices=(
                                         (True, 'Oui'),
                                         (False, 'Non'),
                                     ))


class Apothicaire(Classe_ag):
    medecine = IntegerRangeField(default=0, min_value=1,
                                 max_value=100)
    chirurgie = IntegerRangeField(default=0, min_value=1,
                                  max_value=100)
    poison = IntegerRangeField(default=0, min_value=1,
                               max_value=100)
    guerisseur = models.BooleanField(default=False,
                                     choices=(
                                         (True, 'Oui'),
                                         (False, 'Non'),
                                     ))
    alchimie = IntegerRangeField(default=0, min_value=1,
                                 max_value=100)
    equitation = IntegerRangeField(default=0, min_value=1,
                                   max_value=100)
    maitr_scalpel = models.BooleanField(default=False,
                                        choices=(
                                            (True, 'Oui'),
                                            (False, 'Non'),
                                        ))
    lancer_fioles = models.BooleanField(default=False,
                                        choices=(
                                            (True, 'Oui'),
                                            (False, 'Non'),
                                        ))
    maitr_guerisseur = models.BooleanField(default=False,
                                           choices=(
                                               (True, 'Oui'),
                                               (False, 'Non'),
                                           ))
    enfumeur = models.BooleanField(default=False,
                                   choices=(
                                       (True, 'Oui'),
                                       (False, 'Non'),
                                   ))
