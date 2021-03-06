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
    list_display = ('id', 'username', 'email')
    list_filter = ['groups']
    list_display_links = ('id', 'username')
    save_as = True
    save_on_top = True
    search_fields = ['username', 'email']

admin.site.unregister(User)
admin.site.register(User, UserAdministration)


class ProfileAdministration(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(UserProfile, ProfileAdministration)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% FICHES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class FicheAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'createur')
    list_filter = ['createur', 'profession', 'nom']
    list_display_links = ('id', 'nom')
    save_as = True
    save_on_top = True
    search_fields = ['nom', 'prenom', 'sexe', 'profession']
admin.site.register(Fiche, FicheAdmin)


class GalleriePersoAdmin(admin.ModelAdmin):
    list_display = ('nom_perso', 'id')

admin.site.register(GalleriePerso, GalleriePersoAdmin)

class ImagePersoAdmin(admin.ModelAdmin):
    list_display = ('nom_perso', 'id')

admin.site.register(ImagePerso, ImagePersoAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% OBJETS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #
class ObjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'qualite', 'id')

admin.site.register(Objet, ObjetAdmin)


class ArmureAdmin(admin.ModelAdmin):
    list_display = ('get_nom', 'membre', 'id')

admin.site.register(Armure, ArmureAdmin)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_nom', 'id')

admin.site.register(Case, CaseAdmin)


class InventaireAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

admin.site.register(Inventaire, InventaireAdmin)


class EquipementAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')

admin.site.register(Equipement, EquipementAdmin)


class EnchantementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'id')

admin.site.register(Enchantement, EnchantementAdmin)


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

class RabatteurAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Rabatteur, RabatteurAdmin)


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


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% QUETES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class QueteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'difficulte', 'id')
    form = QueteForm

admin.site.register(Quete, QueteAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% MISSIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class OperationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'id')
    form = OperationForm

admin.site.register(Operation, OperationAdmin)


class MissionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'operation', 'lieu', 'type_mis', 'id')
    form = MissionForm

admin.site.register(Mission, MissionAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% SORTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom', 'id')
    form = ClasseForm

admin.site.register(Classe, ClasseAdmin)


class SortAdmin(admin.ModelAdmin):
    list_display = ('nom', 'id')
    form = SortForm

admin.site.register(Sort, SortAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% IMAGES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class ImageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'id')
    form = ImageForm

admin.site.register(Image, ImageAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% BOURSES %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class BourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'argent')
    form = BourseForm

admin.site.register(Bourse, BourseAdmin)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% HABITATIONS %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class PieceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    form = PieceForm

admin.site.register(Piece, PieceAdmin)


class EtageAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero')
    form = EtageForm

admin.site.register(Etage, EtageAdmin)


class MaisonAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    form = MaisonForm

admin.site.register(Maison, MaisonAdmin)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONSEIL %%%%%%%%%%%%%%%%%%%%%%%%%%%%% #

class LegendeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    form = LegendeForm

admin.site.register(Legende, LegendeAdmin)
