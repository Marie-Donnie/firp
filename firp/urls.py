from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from fiches import views

urlpatterns = [
    # General
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    # Users
    url(r'^utilisateurs/$', views.users,
        name='utilisateurs'),
    url(r'^utilisateurs/gestion_profil/$', views.profile,
        name='gestion_profil'),
    url(r'^utilisateurs/(?P<user_id>\d+)/$', views.aff_user,
        name='utilisateur'),
    # Fiches
    url(r'^personnages/$', views.personnages,
        name='personnages'),
    url(r'^personnages/search=(?P<requete>)$', views.personnages,
        name='personnages'),
    url(r'^fiches/(?P<fiche_id>\d+)/$', views.detail_fiche,
        name='detail_fiche'),
    url(r'^fiches/editer_fiche/(?P<fiche_id>\d+)/$', views.edit_fiche,
        name='editer_fiche'),
    url(r'^fiches/supprimer_fiche/(?P<fiche_id>\d+)/$', views.delete_fiche,
        name='supprimer_fiche'),
    url(r'^fiches/creer/$', views.creer_fiche, name='creer_fiche'),
    # Objets
    url(r'^objets/$', views.objets, name='objets'),
    url(r'^objets/creer_objet/$', views.creer_objet, name='creer_objet'),
    url(r'^objets/creer_armure/$', views.creer_armure, name='creer_armure'),
    url(r'^objets/creer_case/$', views.creer_case, name='creer_case'),
    url(r'^objets/creer_equipement/$', views.creer_equipement,
        name='creer_equipement'),
    url(r'^objets/creer_inventaire/$', views.creer_inventaire,
        name='creer_inventaire'),
    url(r'^objets/objet/(?P<objet_id>\d+)/$', views.detail_objet,
        name='detail_objet'),
    url(r'^objets/armure/(?P<armure_id>\d+)/$', views.detail_armure,
        name='detail_armure'),
    url(r'^objets/objet/(?P<objet_id>\d+)/tooltip/$', views.tooltip_objet,
        name='tooltip_objet'),
    url(r'^objets/armure/(?P<armure_id>\d+)/tooltip/$', views.tooltip_armure,
        name='tooltip_armure'),
    url(r'^objets/editer_objet/(?P<objet_id>\d+)/$', views.edit_objet,
        name='editer_objet'),
    url(r'^objets/editer_armure/(?P<armure_id>\d+)/$', views.edit_armure,
        name='editer_armure'),
    url(r'^objets/editer_case/(?P<case_id>\d+)/$', views.edit_case,
        name='editer_case'),
    url(r'^objets/editer_inventaire/(?P<inventaire_id>\d+)/$',
        views.edit_inventaire, name='editer_inventaire'),
    url(r'^objets/editer_equipement/(?P<equipement_id>\d+)/$',
        views.edit_equipement, name='editer_equipement'),
    # RPG
    url(r'^', include('fiches.rpg.avant_garde.urls')),
    # url(r'^avant_garde/creer_perso/(?P<perso_id>\d+)/$', views.creer_base,
    #     name='creer_perso'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
