from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# from fiches.users import CustomUser, CustomUserChangeForm, UserForm

# Register your models here.
from fiches.models import Fiche, UserProfile, Objet, Armure, Case, Inventaire, Equipement


class FicheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'id')

admin.site.register(Fiche, FicheAdmin)


class ObjetAdmin(admin.ModelAdmin):
    list_display = ('nom', 'qualite', 'id')

admin.site.register(Objet, ObjetAdmin)


class ArmureAdmin(admin.ModelAdmin):
    list_display = ('objet', 'membre', 'id')

admin.site.register(Armure, ArmureAdmin)


class CaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'objet')

admin.site.register(Case, CaseAdmin)


class InventaireAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Inventaire, InventaireAdmin)


class EquipementAdmin(admin.ModelAdmin):
    list_display = ('id',)

admin.site.register(Equipement, EquipementAdmin)


class UserAdministration(admin.ModelAdmin):
    list_display = ['username', 'first_name']

admin.site.unregister(User)
admin.site.register(User, UserAdministration)


class ProfileAdministration(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(UserProfile, ProfileAdministration)

# class CustomUserAdmin(UserAdmin):
#     # The forms to add and change user instances

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference the removed 'username' field
#     fieldsets = (
#         (None, {'fields': ('pseudo', 'email', 'password')}),
#         (_('Infos personnelles'), {'fields': ('nom', 'prenom')}),
#         (_('Permissions'), {'fields': ('groups', 'user_permissions')}),
#         (_('Dates importantes'), {'fields': ('naissance', 'creation')}),
#         (_('Autres informations'), {'fields': ('sexe', 'image')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2')}
#         ),
#     )
#     form = CustomUserChangeForm
#     add_form = UserForm
#     list_display = ('pseudo', 'email', 'nom', 'prenom')
#     search_fields = ('pseudo', 'email', 'nom', 'prenom')
#     ordering = ('pseudo', 'nom', 'prenom')

# admin.site.register(CustomUser, CustomUserAdmin)
