from django.conf.urls import url
from fiches.models import Fiche
from fiches.forms import FicheForm
from fiches.rpg.avant_garde import views

urlpatterns = [
    # General
    url(r'^avant_garde$', views.persos_ag, name='afficher_persos'),
    url(r'^avant_garde/creer_perso/$', views.creer_base,
        name='creer_perso'),
]
