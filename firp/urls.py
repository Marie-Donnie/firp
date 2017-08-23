from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from fiches import views

urlpatterns = [
    # General
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^conseils/$', views.conseils, name='conseils'),
    # Users
    url(r'^utilisateurs/$', views.users,
        name='utilisateurs'),
    url(r'^utilisateurs/gestion_profil/$', views.profile,
        name='gestion_profil'),
    url(r'^utilisateurs/(?P<user_id>\d+)/$', views.aff_user,
        name='utilisateur'),
    # Fiches
    url(r'^$', views.index, name='index'),
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
    # Quetes
    url(r'^quetes/$', views.quetes, name='quetes'),
    url(r'^quetes/(?P<quete_id>\d+)/$', views.quete, name='quete'),
    url(r'^quetes/reserver_quete_(?P<quete_id>\d+)/$', views.res_quete,
        name='reserver_quete'),
    # RPG
    url(r'^', include('fiches.rpg.avant_garde.urls')),
    # Gallery
    url(r'^gallerie/$', views.gallery, name='gallerie'),
    url(r'^gallerie/rechercher/$', views.gallery_search,
        name='rechercher_gallerie'),
    # Campagnes
    url(r'campagnes/$', views.campagnes, name='campagnes'),
    url(r'campagnes/(?P<campagne_id>\d+)/$', views.campagne, name='campagne'),
    url(r'campagnes/(?P<campagne_id>\d+)/(?P<mission_id>\d+)/$', views.mission,
        name='mission'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
