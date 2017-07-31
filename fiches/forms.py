from django.forms import ModelForm
from django import forms
from captcha.fields import ReCaptchaField
from fiches.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['naissance', 'image', 'user']
        widgets = {'user': forms.HiddenInput()}


class AllauthSignupForm(forms.Form):

    captcha = ReCaptchaField()

    def signup(self, request, user):
        """ Required, or else it throws deprecation warnings """
        pass


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class FicheForm(ModelForm):

    class Meta:
        model = Fiche
        fields = ['nom', 'prenom', 'autres_prenoms', 'titre',
                  'autres_titres', 'sexe', 'race', 'taille',
                  'poids', 'c_yeux', 'c_cheveux', 'signes_dis',
                  'profession', 'medailles', 'etat', 'pj',
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
                   'main_dir': forms.RadioSelect(),
                   'equipement': forms.HiddenInput(), }


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
        fields = ['nombre', 'objet', 'createur']
        widgets = {'createur': forms.HiddenInput(), }
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


class QueteForm(ModelForm):

    class Meta:
        model = Quete
        fields = '__all__'
        prefix = 'quete'
        widgets = {'objectif': forms.Textarea(),
                   'etat': forms.RadioSelect(), }
