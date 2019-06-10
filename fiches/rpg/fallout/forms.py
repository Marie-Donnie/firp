from django.forms import ModelForm
from django import forms
from fiches.rpg.fallout.models import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class PersonnageForm(ModelForm):

    class Meta:
        model = Personnage
        fields = '__all__'
        prefix = 'perso'
        widgets = {'inventaire': forms.Textarea(),
                   'description': forms.Textarea(),
                   'historique': forms.Textarea(),
                   'pj': forms.RadioSelect(), }

class EquipementForm(ModelForm):

    class Meta:
        model = Equipement
        fields = '__all__'
        prefix = 'equipement'
        widgets = {'description': forms.Textarea(),
                   'createur': forms.HiddenInput(), }
