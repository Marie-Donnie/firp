from django.forms import ModelForm
from models import *


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


class ApothicaireForm(ModelForm):

    class Meta:
        model = Apothicaire
        fields = '__all__'
        prefix = 'apothicaire'
