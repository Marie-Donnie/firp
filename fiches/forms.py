from fiches.models import Fiche, UserProfile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['naissance', 'image', 'user']
        widgets = {'user': forms.HiddenInput()}


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        prefix = 'user'
        # "__all__"


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    prenom = forms.CharField(required=True)
    nom = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email',
                  'prenom', 'nom')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']

        if commit:
            user.save()

        return user


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
                  'afficher_inventaire', 'image', 'createur']
        widgets = {'createur': forms.HiddenInput(),
                   'inventaire': forms.Textarea(),
                   'description': forms.Textarea(),
                   'historique': forms.Textarea(),
                   'relations': forms.Textarea(),
                   'autres_titres': forms.Textarea(),
                   'medailles': forms.Textarea(), }
