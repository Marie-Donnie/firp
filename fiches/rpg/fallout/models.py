# coding=utf-8
from django.db import models
from django.conf import settings
from fiches.functions import IntegerRangeField

class Personnage(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    surnom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Homme"),
                                ('f', "Femme")
                            )),
                            default="h")
    age = models.SmallIntegerField(default=1)
    origine = models.CharField(max_length=50,
                               default='Inconnue')
    race = models.CharField(max_length=50,
                            default="Humaine")
    description = models.CharField(max_length=6000,
                                   default='A venir')
    historique = models.CharField(max_length=6000,
                                  default='A venir')
    ex_prof = models.CharField(max_length=50,
                               default='Inconnue')
    force = IntegerRangeField(default=1, min_value=1,
                              max_value=10)
    perce = IntegerRangeField(default=1, min_value=1,
                              max_value=10)
    endu = IntegerRangeField(default=1, min_value=1,
                             max_value=10)
    charisme = IntegerRangeField(default=1, min_value=1,
                                 max_value=10)
    intell = IntegerRangeField(default=1, min_value=1,
                               max_value=10)
    agi = IntegerRangeField(default=1, min_value=1,
                            max_value=10)
    chance = IntegerRangeField(default=1, min_value=1,
                                  max_value=10)
    pv = models.SmallIntegerField(default=11)
    pv_max = models.SmallIntegerField(default=11)
    resis_rad = models.SmallIntegerField(default=0)
    rad = models.SmallIntegerField(default=0)
    niveau = models.SmallIntegerField(default=1)
    xp = models.SmallIntegerField(default=0)
    feu = IntegerRangeField(default=1, min_value=1,
                                   max_value=100)
    energie = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    melee = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    crochetage = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    discours = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    discretion = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    explosifs = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    nues = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    medecine = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    reparation = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    sciences = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    survie = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    troc = IntegerRangeField(default=1, min_value=1,
                                max_value=100)
    etat = models.CharField(max_length=800,
                                 null=True,
                                 blank=True,
                                 default='Sans')

    image = models.ImageField(upload_to='images/persos',
                              default='images/site/no-image.png')
    pj = models.CharField(max_length=1,
                          choices=((
                              ('p', "Personnage joué"),
                              ('n', "Personnage non joué")
                          )),
                          default="p")
    talents = models.ManyToManyField('Talents')
    inventaire = models.CharField(max_length=6000,
                                  null=True,
                                  blank=True,
                                  default='Sans')
    equipement = models.CharField(max_length=6000,
                                  null=True,
                                  blank=True,
                                  default='Sans')
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='fallout',
                                 on_delete=models.CASCADE)

    class Meta:
        ordering = ["nom", "prenom"]
        permissions = (("fallout", "A accès à fallout"),)

    def __unicode__(self):
        return u'%s' % (self.nom)


class Talent(models.Model):
    nom = models.CharField(max_length=50, default="Aucun")
    description = models.CharField(max_length=300)
    requis = models.CharField(max_length=300)

    class Meta:
        ordering = ["nom"]
        default_related_name = "avantage"

    def __unicode__(self):
        return u'%s' % (self.nom)
