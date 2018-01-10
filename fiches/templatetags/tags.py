from django import template
from fiches.rpg.avant_garde.models import *

register = template.Library()

# AVANT-GARDE


@register.inclusion_tag('rpg/avant_garde/template_classe.html')
def return_line(classe, fiche):
    afficher = "afficher_" + classe
    cl = eval(classe.capitalize())
    ident = cl.objects.select_related().filter(perso=fiche.id).first().id

    return {'f': fiche, 'afficher': afficher, 'ident': ident}
