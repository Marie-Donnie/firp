from django.forms import ModelForm
from django import forms
from captcha.fields import ReCaptchaField
from fiches.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),
                   'affichage_date': forms.RadioSelect(), }


class AllauthSignupForm(forms.Form):

    captcha = ReCaptchaField()

    def signup(self, request, user):
        """ Required, or else it throws deprecation warnings """
        pass


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class FicheForm(ModelForm):

    class Meta:
        model = Fiche
        fields = ['nom', 'prenom', 'autres_prenoms', 'ne', 'titre',
                  'autres_titres', 'sexe', 'race', 'taille',
                  'poids', 'c_yeux', 'c_cheveux', 'signes_dis',
                  'profession', 'medailles', 'etat', 'pj',
                  'jour_de_naissance', 'mois_de_naissance',
                  'annee_de_naissance', 'zone_de_naissance',
                  'ville_de_naissance', 'zone_de_residence',
                  'ville_de_residence', 'description', 'historique',
                  'inventaire', 'relations',
                  'competences', 'pseudo_du_personnage',
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
        fields = '__all__'
        prefix = 'objet'
        widgets = {'description': forms.Textarea(),
                   'createur': forms.HiddenInput(), }


class ArmureForm(ModelForm):

    class Meta:
        model = Armure
        fields = '__all__'
        prefix = 'armure'
        widgets = {'effet': forms.Textarea(), }


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
        fields = '__all__'
        prefix = 'equipement'


class EnchantementForm(ModelForm):

    class Meta:
        model = Enchantement
        fields = '__all__'
        prefix = 'enchantement'


class QueteForm(ModelForm):

    class Meta:
        model = Quete
        fields = '__all__'
        prefix = 'quete'
        widgets = {'objectif': forms.Textarea(),
                   'etat': forms.RadioSelect(), }


class PrendreQueteForm(ModelForm):

    class Meta:
        model = Quete
        fields = ['etat', 'reservee']
        widgets = {'etat': forms.HiddenInput(), }


class OperationForm(ModelForm):

    class Meta:
        model = Operation
        fields = '__all__'


class MissionForm(ModelForm):

    class Meta:
        model = Mission
        fields = '__all__'
        widgets = {'objectif': forms.Textarea(),
                   'participants': forms.Textarea(),
                   'deroulement': forms.Textarea(), }


class ClasseForm(ModelForm):

    class Meta:
        model = Classe
        fields = '__all__'
        widgets = {'principes': forms.Textarea()}


class SortForm(ModelForm):

    class Meta:
        model = Sort
        fields = '__all__'
        widgets = {'effet': forms.Textarea()}
