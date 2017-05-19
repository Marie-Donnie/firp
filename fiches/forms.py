from fiches.models import Fiche, UserProfile
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserProfileForm(ModelForm):
    # pseudo = forms.CharField(max_length=150)
    # mot_de_passe = forms.CharField(max_length=32, widget=forms.PasswordInput)
    # email = forms.EmailField()
    # prenom = forms.CharField(max_length=30)
    # nom = forms.CharField(max_length=30)
    # naissance = forms.DateField()
    # class Meta:
    #     model = User
    #     fields = ['naissance', 'image']

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user')
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     self.user = user
    class Meta:
        model = UserProfile
        exclude = ['user']
        fields = ['image', 'naissance']
        prefix = 'userprofile'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        prefix = 'user'
        # "__all__"


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    birthday = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthday = self.cleaned_data['birthday']

        if commit:
            user.save()

        return user


class FicheForm(ModelForm):

    class Meta:
        model = Fiche
        fields = ['nom', 'prenom', 'autres_prenoms', 'titre',
                  'autres_titres', 'sexe', 'race', 'taille',
                  'poids', 'profession', 'medaille', 'etat', 'pj',
                  'jour_de_naissance', 'mois_de_naissance',
                  'annee_de_naissance', 'zone_de_naissance',
                  'ville_de_naissance', 'zone_de_residence',
                  'ville_de_residence', 'description', 'historique',
                  'inventaire', 'relations', 'pseudo', 'aff_createur',
                  'aff_inventaire', 'image', 'createur']
        widgets = {'createur': forms.HiddenInput(),
                   'inventaire': forms.Textarea(),
                   'description': forms.Textarea(),
                   'historique': forms.Textarea(),
                   'relations': forms.Textarea()}
