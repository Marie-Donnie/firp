from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from fiches.users import CustomUser, CustomUserChangeForm, UserForm

# Register your models here.
from fiches.models import Fiche, User


class FicheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'id')

admin.site.register(Fiche, FicheAdmin)


class UserAdministration(admin.ModelAdmin):
    list_display = ('user', 'naissance')

admin.site.register(User, UserAdministration)

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
