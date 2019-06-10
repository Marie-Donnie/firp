from django.forms import ModelForm
from django import forms
from dal import autocomplete
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from fiches.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(),
                   'affichage_date': forms.RadioSelect(), }


class AllauthSignupForm(forms.Form):

    captcha = ReCaptchaField(widget=ReCaptchaWidget())

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
                  'competences', 'autres_informations',
                  'pseudo_du_personnage',
                  'afficher_pseudo', 'afficher_createur',
                  'afficher_inventaire', 'afficher_bourse', 'image', 'main_dir',
                  'inventaire_fdg', 'equipement', 'bourse', 'createur',
                  'gallerie']
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
                   'afficher_bourse': forms.CheckboxInput(),
                   'pj': forms.RadioSelect(),
                   'main_dir': forms.RadioSelect(),
                   'equipement': forms.HiddenInput(),
                   'bourse': forms.HiddenInput(), }


class ImagePersoForm(ModelForm):

    class Meta:
        model = ImagePerso
        fields = '__all__'
        widgets = {'nom_perso': forms.HiddenInput(),
                   'definition': forms.Textarea(),
                   'gallerie': forms.HiddenInput(), }


class GalleriePersoForm(ModelForm):

    class Meta:
        model = GalleriePerso
        fields = '__all__'



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
        widgets = {'createur': forms.HiddenInput(), }
        prefix = 'enchantement'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUETES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

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


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% MISSIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

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
                   'deroulement': forms.Textarea(),
                   'dirigeant': autocomplete.ModelSelect2(url='fiche-autocomplete'), }


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% SORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

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


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class ImageForm(ModelForm):

    class Meta:
        model = Image
        fields = '__all__'



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMERCES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class BourseForm(ModelForm):

    class Meta:
        model = Bourse
        fields = '__all__'


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% HABITATIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class PieceForm(ModelForm):

    class Meta:
        model = Piece
        fields = '__all__'
        widgets = {'description': forms.Textarea(),
                   'createur': forms.HiddenInput(),
                   'mobilier': forms.Textarea(), }


class EtageForm(ModelForm):

    class Meta:
        model = Etage
        fields = '__all__'
        widgets = {'createur': forms.HiddenInput(), }


class MaisonForm(ModelForm):

    class Meta:
        model = Maison
        fields = '__all__'
        widgets = {'proprietaire': forms.HiddenInput(),
                   'description': forms.Textarea(),
                   'habitants': forms.Textarea(),
                   'materiel': forms.Textarea(),
                   'prod': forms.Textarea(),
                   'afficher_pseudo': forms.CheckboxInput(), }


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMERCES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class LegendeForm(ModelForm):

    class Meta:
        model = Legende
        fields = '__all__'
        widgets = {'description': forms.Textarea(), }
