# coding=utf-8
from django.db import models
from fiches.functions import IntegerRangeField


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

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
