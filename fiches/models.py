# coding=utf-8
from django.db import models
from django.forms import ModelForm
from django.conf import settings
from django.utils import timezone


class IntegerRangeField(models.SmallIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None,
                 max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.SmallIntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


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
    autresprenoms = models.CharField(max_length=200,
                                     default='Aucun')
    titre = models.CharField(max_length=75,
                             default='Aucun')
    autrestitres = models.CharField(max_length=500,
                                    default='Aucun')
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Masculin"),
                                ('f', "Féminin")
                            )),
                            default="Masculin")
    race = models.CharField(max_length=40,
                            default='Humaine')
    taille = models.FloatField(default='1.70')
    poids = models.FloatField(default='70')
    profession = models.CharField(max_length=75,
                                  default='Prostipute')
    medaille = models.CharField(max_length=3000,
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
    jour_naissance = IntegerRangeField(default='1', min_value=1,
                                       max_value=31)
    mois_naissance = IntegerRangeField(default='1', min_value=1,
                                       max_value=12)
    annee_naissance = IntegerRangeField(default='0', min_value=-32000,
                                        max_value=100)
    zone_naissance = models.SmallIntegerField(choices=ZONES_CHOIX)
    description = models.CharField(max_length=3000,
                                   default='A venir')
    historique = models.CharField(max_length=3000,
                                  default='A venir')
    image = models.ImageField(upload_to='images/persos/',
                              default='images/site/no-image.png')


class FicheForm(ModelForm):
    class Meta:
        model = Fiche
        fields = ['nom', 'prenom', 'autresprenoms', 'titre',
                  'autrestitres', 'sexe', 'race', 'taille',
                  'poids', 'profession', 'medaille', 'etat', 'pj',
                  'jour_naissance', 'mois_naissance', 'annee_naissance',
                  'zone_naissance', 'description', 'historique', 'image']


class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='images/users/',
                              default='images/site/no-image.png')
    naissance = models.DateField()
    creation = models.DateTimeField(default=timezone.now)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user', 'naissance', 'image']
