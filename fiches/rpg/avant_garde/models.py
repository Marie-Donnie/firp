# coding=utf-8
from django.db import models
from django.conf import settings
from fiches.functions import IntegerRangeField

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


class Campagne(models.Model):
    nom = models.CharField(max_length=50)
    mois_debut = IntegerRangeField(default='1', min_value=1,
                                   max_value=12)
    mois_fin = IntegerRangeField(default='1', min_value=1,
                                 max_value=12)
    annee_debut = IntegerRangeField(default='37', min_value=24,
                                    max_value=100)
    annee_fin = IntegerRangeField(default='37', min_value=24,
                                  max_value=100)
    objectif = models.CharField(max_length=100,
                                default='Tuer.')
    fini = models.BooleanField(default=False,
                               choices=(
                                   (True, 'Oui'),
                                   (False, 'Non'),
                               ))
    image = models.ImageField(upload_to='images/rpg/campagne',
                              default='images/site/avant-garde.jpg')

    def __unicode__(self):
        return u'%s' % (self.nom)


class Avant_garde(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Homme"),
                                ('f', "Femme")
                            )),
                            default="h")
    jour_de_naissance = IntegerRangeField(default='1', min_value=1,
                                          max_value=31)
    mois_de_naissance = IntegerRangeField(default='1', min_value=1,
                                          max_value=12)
    annee_de_naissance = IntegerRangeField(default='0', min_value=-32000,
                                           max_value=100)
    ville_de_naissance = models.CharField(max_length=50,
                                          default='Inconnue')
    race = models.CharField(max_length=1,
                            choices=((
                                    ('n', "Nain"),
                                    ('e', "Haut-elfe"),
                                    ('h', "Humain")
                                )),
                            default="h")
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
    autre_metier = models.CharField(max_length=30,
                                    default="Aucun")
    grade_rp = models.SmallIntegerField(choices=((
        (1, "Soldat"),
        (2, "Caporal"),
        (3, "Sergent"),
        (4, "Lieutenant"),
        (5, "Capitaine")
    )),
                                        default=1)
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
    pv_max = models.SmallIntegerField(default=11)
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
    image = models.ImageField(upload_to='images/persos',
                              default='images/site/no-image.png')
    classe = models.SmallIntegerField(choices=((
        (1, "Fantassin"),
        (2, "Arbalétrier"),
        (3, "Eclaireur"),
        (4, "Apothicaire de combat"),
        (5, "Apprenti sorcier")
    )),
                                       default=1)
    etat = models.CharField(max_length=1,
                            choices=((
                              ('v', "Vivant"),
                              ('m', "Mort"),
                              ('d', "Disparu")
                            )),
                            default="v")
    pj = models.CharField(max_length=1,
                          choices=((
                              ('p', "Personnage joué"),
                              ('n', "Personnage non joué")
                          )),
                          default="p")
    avants = models.ManyToManyField('Avantages')
    desavants = models.ManyToManyField('Desavantages')
    inventaire = models.CharField(max_length=800,
                                  null=True,
                                  blank=True,
                                  default='Sans')
    equipement = models.CharField(max_length=800,
                                  null=True,
                                  blank=True,
                                  default='Sans')
    peur = models.CharField(max_length=80,
                            null=True,
                            blank=True,
                            default='Sans')
    dependances = models.CharField(max_length=80,
                                   null=True,
                                   blank=True,
                                   default='Sans')
    campagne = models.ManyToManyField(Campagne,
                                      blank=True)
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='avant_garde')

    class Meta:
        ordering = ["nom", "prenom"]
        permissions = (("avant_garde", "A accès à l'avant-garde"),)

    def __unicode__(self):
        return u'%s' % (self.nom)


class Fantassin(models.Model):
    intim = IntegerRangeField(default=0, min_value=0,
                              max_value=100)
    parer_fleches = IntegerRangeField(default=0, min_value=0,
                                      max_value=100)
    athle_resi = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Athlétisme"),
        (3, "Résistant")
    )),
                                          default=1)
    escalade = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    cc = IntegerRangeField(default=0, min_value=0,
                           max_value=100)
    prot = IntegerRangeField(default=0, min_value=0,
                             max_value=100)
    epe_craned = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Epéiste"),
        (3, "Crâne dûr")
    )),
                                          default=1)
    equitation = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    glaive_lourde = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Maîtrise du glaive"),
        (3, "Maîtrise de l'armure lourde")
    )),
                                          default=1)
    feroce_impla = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Féroce"),
        (3, "Implacable")
    )),
                                          default=1)
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='fantassin')

    def __unicode__(self):
        return u'%s' % (self.perso.nom)


class Apothicaire(models.Model):
    medecine = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    chirurgie = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    poison = IntegerRangeField(default=0, min_value=0,
                               max_value=100)
    guerisseur = models.BooleanField(default=False,
                                     choices=(
                                         (True, 'Oui'),
                                         (False, 'Non'),
                                     ))
    alchimie = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    equitation = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    scalpel_fioles = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Maîtrise du scalpel"),
        (3, "Art du lancer de fioles")
    )),
                                          default=1)
    guerisseur_enfum = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Maître guérisseur"),
        (3, "Enfumeur")
    )),
                                          default=1)
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='apothicaire')

    def __unicode__(self):
        return u'%s' % (self.perso.nom)


class Arbaletrier(models.Model):
    focalisation = IntegerRangeField(default=0, min_value=0,
                                     max_value=100)
    couvert = IntegerRangeField(default=0, min_value=0,
                                max_value=100)
    escalade = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    coup_crit = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    vigilance = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    equitation = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    dissimulation = IntegerRangeField(default=0, min_value=0,
                                      max_value=100)
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='arbaletrier')

    def __unicode__(self):
        return u'%s' % (self.perso.nom)


class Eclaireur(models.Model):
    dissimulation = IntegerRangeField(default=0, min_value=0,
                                      max_value=100)
    vigilance = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    aigle_vif = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Œil d'aigle"),
        (3, "Vif")
    )),
                                          default=1)
    escalade = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    equitation = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    pistage = IntegerRangeField(default=0, min_value=0,
                                max_value=100)
    deguisement = IntegerRangeField(default=0, min_value=0,
                                    max_value=100)
    vigilant_rx = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Vigilant"),
        (3, "Réflexes éclaireurs")
    )),
                                          default=1)
    natation = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    contorsion = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    trap = IntegerRangeField(default=0, min_value=0,
                             max_value=100)
    depl_silenc = IntegerRangeField(default=0, min_value=0,
                                    max_value=100)
    assassin = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    maitr_anim = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    silen_rodeur = models.SmallIntegerField(choices=((
        (1, "Niveau inférieur"),
        (2, "Art de la mort silencieuse"),
        (3, "Rôdeur")
    )),
                                          default=1)
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='eclaireur')

    def __unicode__(self):
        return u'%s' % (self.perso.nom)


class Sorcier(models.Model):
    boule_feu = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    trait_feu = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    contresort = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    nova_feu = IntegerRangeField(default=0, min_value=0,
                                 max_value=100)
    souffle_dragon = IntegerRangeField(default=0, min_value=0,
                                       max_value=100)
    portail = IntegerRangeField(default=0, min_value=0,
                                max_value=100)
    pilier_feu = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    explo_pyro = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    transfert = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    desamorcer_pieges = IntegerRangeField(default=0, min_value=0,
                                          max_value=100)
    enchant = IntegerRangeField(default=0, min_value=0,
                                max_value=100)
    pluie_feu = IntegerRangeField(default=0, min_value=0,
                                  max_value=100)
    bombe_vivante = IntegerRangeField(default=0, min_value=0,
                                      max_value=100)
    annul_male = IntegerRangeField(default=0, min_value=0,
                                   max_value=100)
    ana_magique = IntegerRangeField(default=0, min_value=0,
                                    max_value=100)
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='sorcier')

    def __unicode__(self):
        return u'%s' % (self.perso.nom)


class Avantages(models.Model):
    nom = models.CharField(max_length=50, default="Aucun")
    description = models.CharField(max_length=300)
    points = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["nom"]
        default_related_name = "avantage"

    def __unicode__(self):
        return u'%s' % (self.nom)


class Desavantages(models.Model):
    nom = models.CharField(max_length=50, default="Aucun")
    description = models.CharField(max_length=300)
    points = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["nom"]
        default_related_name = "désavantage"

    def __unicode__(self):
        return u'%s' % (self.nom)
