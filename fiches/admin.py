from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from fiches.models import *
from fiches.forms import *
from fiches.rpg.avant_garde.models import *
from fiches.rpg.avant_garde.forms import *


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% USERS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class UserAdministration(admin.ModelAdmin):
    list_display = ['username', 'first_name']

admin.site.unregister(User)
admin.site.register(User, UserAdministration)


class ProfileAdministration(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(UserProfile, ProfileAdministration)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class FicheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'id')

admin.site.register(Fiche, FicheAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% OBJETS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class ObjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'qualite', 'id')

admin.site.register(Objet, ObjetAdmin)


class ArmureAdmin(admin.ModelAdmin):
    list_display = ('get_nom', 'membre', 'id')

admin.site.register(Armure, ArmureAdmin)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_nom')

admin.site.register(Case, CaseAdmin)


class InventaireAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Inventaire, InventaireAdmin)


class EquipementAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Equipement, EquipementAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% RPG %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class A_gAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom')

admin.site.register(Avant_garde, A_gAdmin)


class FantassinAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Fantassin, FantassinAdmin)


class EclaireurAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Eclaireur, EclaireurAdmin)


class ArbaletrierAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Arbaletrier, ArbaletrierAdmin)


class ApothicaireAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Apothicaire, ApothicaireAdmin)


class SorcierAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Sorcier, SorcierAdmin)


class AvantageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'points', 'description', 'id')

admin.site.register(Avantages, AvantageAdmin)


class DesavantageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'points', 'description', 'id')

admin.site.register(Desavantages, DesavantageAdmin)


class CampagneAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    form = CampagneForm

admin.site.register(Campagne, CampagneAdmin)


class QueteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'difficulte', 'id')
    form = QueteForm

admin.site.register(Quete, QueteAdmin)
