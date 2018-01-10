from django.forms import ModelForm
from django import forms
from fiches.rpg.avant_garde.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class Avant_GardeForm(ModelForm):

    class Meta:
        model = Avant_garde
        fields = '__all__'
        prefix = 'ag'

# class Classe_agForm(ModelForm):

#     class Meta:
#         model = Classe_ag
#         fields = '__all__'
#         prefix = 'class_ag'


class FantassinForm(ModelForm):

    class Meta:
        model = Fantassin
        fields = '__all__'
        prefix = 'fantassin'
        widgets = {'perso': forms.HiddenInput()}


class ApothicaireForm(ModelForm):

    class Meta:
        model = Apothicaire
        fields = '__all__'
        prefix = 'apothicaire'
        widgets = {'perso': forms.HiddenInput()}


class ArbaletrierForm(ModelForm):

    class Meta:
        model = Arbaletrier
        fields = '__all__'
        prefix = 'arbaletrier'
        widgets = {'perso': forms.HiddenInput()}


class EclaireurForm(ModelForm):

    class Meta:
        model = Eclaireur
        fields = '__all__'
        prefix = 'eclaireur'
        widgets = {'perso': forms.HiddenInput()}


class SorcierForm(ModelForm):

    class Meta:
        model = Sorcier
        fields = '__all__'
        prefix = 'sorcier'
        widgets = {'perso': forms.HiddenInput()}

class RabatteurForm(ModelForm):

    class Meta:
        model = Rabatteur
        fields = '__all__'
        prefix = 'rabatteur'
        widgets = {'perso': forms.HiddenInput()}


class CampagneForm(ModelForm):

    class Meta:
        model = Campagne
        fields = '__all__'
        prefix = 'campagne'
        widgets = {'objectif': forms.Textarea(),
                   'fini': forms.RadioSelect(), }
