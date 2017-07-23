from django.conf.urls import url
from fiches.models import Fiche
from fiches.forms import FicheForm
from fiches.rpg.avant_garde import views

urlpatterns = [
    # General
    url(r'^avant_garde/$', views.persos_ag, name='avant_garde_persos'),
    url(r'^avant_garde/personnage/(?P<perso_id>\d+)/$', views.detail_perso,
        name='detail_perso'),
    url(r'^avant_garde/editer_personnage/(?P<base_id>\d+)/$',
        views.editer_base, name='editer_perso'),
    url(r'^avant_garde/creer_perso/$', views.creer_base,
        name='creer_perso'),
    url(r'^avant_garde/creer_apothicaire/(?P<perso_id>\d+)/$',
        views.creer_apothicaire, name='creer_apo'),
    url(r'^avant_garde/creer_fantassin/(?P<perso_id>\d+)/$',
        views.creer_fantassin, name='creer_fantassin'),
    url(r'^avant_garde/creer_arbaletrier/(?P<perso_id>\d+)/$',
        views.creer_arbaletrier, name='creer_arbaletrier'),
    url(r'^avant_garde/creer_eclaireur/(?P<perso_id>\d+)/$',
        views.creer_eclaireur, name='creer_eclaireur'),
    url(r'^avant_garde/creer_sorcier/(?P<perso_id>\d+)/$',
        views.creer_sorcier, name='creer_sorcier'),
    url(r'^avant_garde/editer_fantassin/(?P<perso_id>\d+)/$',
        views.edit_fantassin, name='editer_fantassin'),
]
