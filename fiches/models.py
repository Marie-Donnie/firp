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
                                                 default=19,
                                                 null=True)
    ville_de_naissance = models.CharField(max_length=50,
                                          default='Inconnu')
    zone_de_residence = models.SmallIntegerField(choices=ZONES_CHOIX,
                                                 default=19,
                                                 null=True)
    ville_de_residence = models.CharField(max_length=50,
                                          default='Noirebois')
    description = models.CharField(max_length=6000,
                                   default='A venir')
    historique = models.CharField(max_length=6000,
                                  default='A venir')
    inventaire = models.CharField(max_length=6000,
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
