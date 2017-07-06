# coding=utf-8
from django.db import models
from django.conf import settings
from fiches.functions import IntegerRangeField

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #


class Avant_garde(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1,
                            choices=((
                                ('h', "Homme"),
                                ('f', "Femme")
                            )),
                            default="Homme")
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
                            default="Vivant")
    pj = models.CharField(max_length=1,
                          choices=((
                              ('p', "Personnage joué"),
                              ('n', "Personnage non joué")
                          )),
                          default="Personnage joué")
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
    createur = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True,
                                 related_name='avant_garde')

    class Meta:
        ordering = ["nom", "prenom"]
        permissions = (("avant_garde", "A accès à l'avant-garde"),)


class Fantassin(models.Model):
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
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='fantassin')



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
    perso = models.OneToOneField(Avant_garde,
                                 null=True,
                                 related_name='apothicaire')


class Avantages(models.Model):
    nom = models.CharField(max_length=50, default="Aucun")
    description = models.CharField(max_length=100)
    points = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["nom"]
        default_related_name = "avantage"


class Desavantages(models.Model):
    nom = models.CharField(max_length=50, default="Aucun")
    description = models.CharField(max_length=100)
    points = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ["nom"]
        default_related_name = "désavantage"
