from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from fiches.models import *
from fiches.rpg.avant_garde.models import *


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
    list_display = ('id',)

admin.site.register(Avant_garde, A_gAdmin)


class FantassinAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Fantassin, FantassinAdmin)


class ApothicaireAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Apothicaire, ApothicaireAdmin)


class AvantagesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'points', 'description', 'id')

admin.site.register(Avantages, AvantagesAdmin)
