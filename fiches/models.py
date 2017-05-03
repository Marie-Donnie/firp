# coding=utf-8
from django.db import models
from django.forms import ModelForm

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
    # prenom2 = models.CharField(max_length=50,
    #                            default='')
    # prenom3 = models.CharField(max_length=50,
    #                            default='')
    # prenom4 = models.CharField(max_length=50,
    #                            default='')
    # prenom5 = models.CharField(max_length=50,
    #                            default='')
    # prenom6 = models.CharField(max_length=50,
    #                            default='')
    # prenom7 = models.CharField(max_length=50,
    #                            default='')
    # prenom8 = models.CharField(max_length=50,
    #                            default='')
    autresprenoms = models.CharField(max_length=200,
                                     default='')
    titre = models.CharField(max_length=75,
                             default='Aucun')
    # titre2 = models.CharField(max_length=75,
    #                           default='')
    # titre3 = models.CharField(max_length=75,
    #                           default='')
    # titre4 = models.CharField(max_length=75,
    #                           default='')
    # titre5 = models.CharField(max_length=75,
    #                           default='')
    # titre6 = models.CharField(max_length=75,
    #                           default='')
    # titre7 = models.CharField(max_length=75,
    #                           default='')
    # titre8 = models.CharField(max_length=75,
    #                           default='')
    autrestitres = models.CharField(max_length=500,
                                    default='')
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Masculin"),
                                ('f', "Féminin")
                            )))
    race = models.CharField(max_length=40,
                            default='Humaine')
    taille = models.FloatField()
    poids = models.FloatField()
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
    jour_naissance = models.SmallIntegerField()
    mois_naissance = models.SmallIntegerField()
    annee_naissance = models.SmallIntegerField()
    zone_naissance = models.SmallIntegerField(choices=ZONES_CHOIX)
    description = models.CharField(max_length=3000,
                                   default='A venir')
    historique = models.CharField(max_length=3000,
                                  default='A venir')
    image = models.ImageField(upload_to='images/',
                              default='images/no-image.png')


class FicheForm(ModelForm):
    class Meta:
        model = Fiche
        fields = ['nom', 'prenom', 'autresprenoms', 'titre',
                  'autrestitres', 'sexe', 'race', 'taille',
                  'poids', 'profession', 'medaille', 'etat', 'pj',
                  'jour_naissance', 'mois_naissance', 'annee_naissance',
                  'zone_naissance', 'description', 'historique', 'image']
