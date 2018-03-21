from django.conf.urls import url
from fiches.models import Fiche
from fiches.forms import FicheForm
from fiches.rpg.avant_garde import views

urlpatterns = [
    # General
    url(r'^avant_garde/$', views.persos_ag, name='avant_garde_persos'),
    url(r'^avant_garde/presentation$', views.presentation, name='avant_garde_pres'),
    url(r'^avant_garde/personnage/(?P<perso_id>\d+)/$', views.detail_perso,
        name='detail_perso'),
    url(r'^avant_garde/editer_personnage/(?P<base_id>\d+)/$',
        views.editer_base, name='editer_perso'),
    url(r'^avant_garde/creer_perso/$', views.creer_base,
        name='creer_perso'),
    url(r'^avant_garde/creer_fantassin/(?P<perso_id>\d+)/$',
        views.creer_fantassin, name='creer_fantassin'),
    url(r'^avant_garde/creer_arbaletrier/(?P<perso_id>\d+)/$',
        views.creer_arbaletrier, name='creer_arbaletrier'),
    url(r'^avant_garde/creer_eclaireur/(?P<perso_id>\d+)/$',
        views.creer_eclaireur, name='creer_eclaireur'),
    url(r'^avant_garde/creer_apothicaire/(?P<perso_id>\d+)/$',
        views.creer_apothicaire, name='creer_apothicaire'),
    url(r'^avant_garde/creer_sorcier/(?P<perso_id>\d+)/$',
        views.creer_sorcier, name='creer_sorcier'),
    url(r'^avant_garde/creer_rabatteur/(?P<perso_id>\d+)/$',
        views.creer_rabatteur, name='creer_rabatteur'),
    url(r'^avant_garde/editer_fantassin/(?P<perso_id>\d+)/$',
        views.edit_fantassin, name='editer_fantassin'),
    url(r'^avant_garde/editer_arbaletrier/(?P<perso_id>\d+)/$',
        views.edit_arbaletrier, name='editer_arbaletrier'),
    url(r'^avant_garde/editer_eclaireur/(?P<perso_id>\d+)/$',
        views.edit_eclaireur, name='editer_eclaireur'),
    url(r'^avant_garde/editer_apothicaire/(?P<perso_id>\d+)/$',
        views.edit_apothicaire, name='editer_apothicaire'),
    url(r'^avant_garde/editer_sorcier/(?P<perso_id>\d+)/$',
        views.edit_sorcier, name='editer_sorcier'),
    url(r'^avant_garde/editer_rabatteur/(?P<perso_id>\d+)/$',
        views.edit_rabatteur, name='editer_rabatteur'),
    url(r'^avant_garde/afficher_fantassin/(?P<classe_id>\d+)/$',
        views.afficher_fantassin, name='afficher_fantassin'),
    url(r'^avant_garde/afficher_arbaletrier/(?P<classe_id>\d+)/$',
        views.afficher_arbaletrier, name='afficher_arbaletrier'),
    url(r'^avant_garde/afficher_eclaireur/(?P<classe_id>\d+)/$',
        views.afficher_eclaireur, name='afficher_eclaireur'),
    url(r'^avant_garde/afficher_apothicaire/(?P<classe_id>\d+)/$',
        views.afficher_apothicaire, name='afficher_apothicaire'),
    url(r'^avant_garde/afficher_sorcier/(?P<classe_id>\d+)/$',
        views.afficher_sorcier, name='afficher_sorcier'),
    url(r'^avant_garde/afficher_rabatteur/(?P<classe_id>\d+)/$',
        views.afficher_rabatteur, name='afficher_rabatteur'),
    url(r'^avant_garde/supprimer_fiche/(?P<classe>\d+)/(?P<classe_id>\d+)/$',
        views.delete_fiche, name='supprimer_fiche'),
]
