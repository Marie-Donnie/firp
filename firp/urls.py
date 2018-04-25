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
    url(r'^en-savoir-plus/$', views.plus, name='plus'),
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
    url(r'^personnages/sort_by/(?P<requete>)$', views.personnages,
        name='personnages'),
    url(r'^fiches/(?P<fiche_id>\d+)/$', views.detail_fiche,
        name='detail_fiche'),
    url(r'^fiches/editer_fiche/(?P<fiche_id>\d+)/$', views.edit_fiche,
        name='editer_fiche'),
    url(r'^fiches/supprimer_fiche/(?P<fiche_id>\d+)/$', views.delete_fiche,
        name='supprimer_fiche'),
    url(r'^fiches/creer/$', views.creer_fiche, name='creer_fiche'),
    url(r'^fiches/bourse/(?P<fiche_id>\d+)/(?P<bourse_id>\d+)/$', views.gerer_bourse,
        name='gerer_bourse'),
    url(r'^fiches/bourse/(?P<fiche_id>\d+)/$', views.creer_bourse,
        name='creer_bourse'),
    url(r'^fiches/rechercher/$', views.personnages, name='rechercher_fiche'),
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
    url(r'^objets/armure/(?P<armure_id>\d+)/(?P<enchant_id>\d+)/tooltip/$', views.tooltip_armure,
        name='tooltip_armure'),
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
    url(r'^objets/editer_equip/(?P<equipement_id>\d+)/$',
        views.edit_equip, name='editer_equip'),
    url(r'^objets/creer_enchantement/$', views.creer_enchantement,
        name='creer_enchantement'),
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
    url(r'^campagnes/$', views.campagnes, name='campagnes'),
    url(r'^campagnes/(?P<campagne_id>\d+)/$', views.campagne, name='campagne'),
    url(r'^campagnes/(?P<campagne_id>\d+)/(?P<mission_id>\d+)/$', views.mission,
        name='mission'),
    url(r'^campagnes/creer_mission/$', views.creer_mission, name='creer_mission'),
    url(r'^campagnes/editer_mission/(?P<mission_id>\d+)/$', views.edit_mission, name='editer_mission'),
    # Sorts
    url(r'^classes/$', views.classes, name='classes'),
    url(r'^classes/(?P<classe_id>\d+)/$', views.sorts, name='sorts'),
    url(r'^classes/(?P<sort_id>\d+)/tooltip/$', views.tooltip_sort,
        name='tooltip_sort'),
    # Images
    url(r'^images/telecharger/$', views.image, name='image_upload'),
    url(r'^images/gallerie/$', views.upload_gallery, name='upload_gallery'),
    # Cartes
    url(r'^cartes/duche/$', views.cartes, name='cartes'),
    url(r'^cartes/duche/quetes_json$', views.json_carte),
    # Habitations
    #url(r'classes/$', views.classes, name='classes'),
    url(r'habitations/creer_maison/(?P<proprietaire_id>\d+)/(?P<type_maison>\d+)/$',
        views.creer_maison, name='creer_maison'),
    url(r'^habitations/$', views.habitations, name='habitations'),
    url(r'^habitations/creer_piece/$', views.creer_piece, name='creer_piece'),
    url(r'^habitations/creer_etage/$', views.creer_etage, name='creer_etage'),
    url(r'^habitations/rechercher/$', views.habitations, name='rechercher_maison'),
    url(r'^habitations/maison/(?P<maison_id>\d+)/$', views.detail_maison,
        name='detail_maison'),
    # Utils
    url(r'^compter_boutiques/$', views.compter_boutiques, name='boutiques'),
    # Autocomplete
    url(r'^fiche-autocomplete/$', views.FicheAutocomplete.as_view(),
        name='fiche-autocomplete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
