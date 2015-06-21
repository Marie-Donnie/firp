from django.contrib import admin

# Register your models here.
from fiches.models import Fiche

class FicheAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'id')

admin.site.register(Fiche, FicheAdmin)
