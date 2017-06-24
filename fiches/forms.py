from fiches.models import *
# Fiche, UserProfile, Objet, Armure, Case, Equipement
# from fiches.models import Inventaire, Rpg, Avant_Garde, Classe
from rpg.avant_garde.models import *
from django.forms import ModelForm
from django import forms


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['naissance', 'image', 'user']
        widgets = {'user': forms.HiddenInput()}


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class FicheForm(ModelForm):

    class Meta:
        model = Fiche
        fields = ['nom', 'prenom', 'autres_prenoms', 'titre',
                  'autres_titres', 'sexe', 'race', 'taille',
                  'poids', 'profession', 'medailles', 'etat', 'pj',
                  'jour_de_naissance', 'mois_de_naissance',
                  'annee_de_naissance', 'zone_de_naissance',
                  'ville_de_naissance', 'zone_de_residence',
                  'ville_de_residence', 'description', 'historique',
                  'inventaire', 'relations', 'pseudo_du_personnage',
                  'afficher_pseudo', 'afficher_createur',
                  'afficher_inventaire', 'image', 'main_dir',
                  'inventaire_fdg', 'equipement', 'createur']
        widgets = {'createur': forms.HiddenInput(),
                   'inventaire': forms.Textarea(),
                   'description': forms.Textarea(),
                   'historique': forms.Textarea(),
                   'relations': forms.Textarea(),
                   'autres_titres': forms.Textarea(),
                   'medailles': forms.Textarea(),
                   'afficher_pseudo': forms.CheckboxInput(),
                   'afficher_createur': forms.CheckboxInput(),
                   'afficher_inventaire': forms.CheckboxInput(),
                   'pj': forms.RadioSelect(),
                   'main_dir': forms.RadioSelect(), }


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% OBJETS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class ObjetForm(ModelForm):

    class Meta:
        model = Objet
        fields = ['nom', 'qualite', 'description', 'prix', 'poids', 'image']
        prefix = 'objet'
        widgets = {'description': forms.Textarea(), }


class ArmureForm(ModelForm):

    class Meta:
        model = Armure
        fields = ['objet', 'effet', 'autres_effets', 'effet_ig',
                  'force', 'intell', 'agi', 'membre', 'armure']
        prefix = 'armure'


class CaseForm(ModelForm):

    class Meta:
        model = Case
        fields = ['nombre', 'objet']
        prefix = 'case'


class InventaireForm(ModelForm):

    class Meta:
        model = Inventaire
        fields = ['cases', 'nom']
        prefix = 'inventaire'


class EquipementForm(ModelForm):

    class Meta:
        model = Equipement
        fields = ['objets', 'nom']
        prefix = 'equipement'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class RpgForm(ModelForm):

    class Meta:
        model = Rpg
        fields = ['nom']
        prefix = 'rpg'


class Avant_GardeForm(RpgForm):

    class Meta:
        model = Avant_garde
        fields = '__all__'
        prefix = 'a_g'


class Classe_agForm(ModelForm):

    class Meta:
        model = Classe_ag
        fields = ['nom']
        prefix = 'class_ag'


class FantassinForm(Classe_agForm):

    class Meta:
        model = Fantassin
        fields = '__all__'
        prefix = 'fantassin'


class ApothicaireForm(Classe_agForm):

    class Meta:
        model = Apothicaire
        fields = '__all__'
        prefix = 'apothicaire'
