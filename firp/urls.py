from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from fiches import views

urlpatterns = [
    # General
    url(r'^admin/', admin.site.urls),
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
    url(r'^personnages/mes_personnages$', views.mes_persos,
        name='mes_personnages'),
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
    url(r'^fiches/gallerie/(?P<fiche_id>\d+)/$', views.upload_gallery_perso, name='gallerie_perso'),
    url(r'^fiches/creer_gallerie/(?P<fiche_id>\d+)/$', views.creer_gallerie, name='creer_gallerie'),
    url(r'^fiches/image/(?P<fiche_id>\d+)/$', views.image_perso, name='image_perso_upload'),
    # Objets
    url(r'^objets/$', views.objets, name='objets'),
    url(r'^objets/objets/creer_objet/$', views.creer_objet, name='creer_objet'),
    url(r'^objets/objets/(?P<objet_id>\d+)/$', views.detail_objet,
        name='detail_objet'),
    url(r'^objets/objets/(?P<objet_id>\d+)/tooltip/$', views.tooltip_objet,
        name='tooltip_objet'),
    url(r'^objets/objets/editer_objet/(?P<objet_id>\d+)/$', views.edit_objet,
        name='editer_objet'),
    url(r'^objets/objets/supprimer_objet/(?P<objet_id>\d+)/$', views.delete_objet,
        name='supprimer_objet'),
    url(r'^objets/armures/creer_armure/$', views.creer_armure, name='creer_armure'),
    url(r'^objets/armures/armure/(?P<armure_id>\d+)/$', views.detail_armure,
        name='detail_armure'),
    url(r'^objets/armures/armure/(?P<armure_id>\d+)/(?P<enchant_id>\d+)/tooltip/$',
        views.tooltip_armure, name='tooltip_armure'),
    url(r'^objets/armures/armure/(?P<armure_id>\d+)/tooltip/$', views.tooltip_armure,
        name='tooltip_armure'),
    url(r'^objets/armures/editer_armure/(?P<armure_id>\d+)/$', views.edit_armure,
        name='editer_armure'),
    url(r'^objets/armures/copier_armure/(?P<armure_id>\d+)/$', views.copier_armure,
        name='copier_armure'),
    url(r'^objets/cases/creer_case/$', views.creer_case, name='creer_case'),
    url(r'^objets/cases/creer_case_perso/(?P<fiche_id>\d+)$', views.creer_case_perso, name='creer_case_perso'),
    url(r'^objets/cases/editer_case/(?P<case_id>\d+)$', views.edit_case,
        name='editer_case'),
    url(r'^objets/cases/(?P<case_id>\d+)/changer_cardinalite/(?P<valeur>-?\d+)$', views.edit_case_number,
        name='changer_cardinalite_case'),
    url(r'^objets/cases/supprimer_case/(?P<case_id>\d+)$', views.delete_case,
        name='supprimer_case'),
    url(r'^objets/inventaires/creer_inventaire/$', views.creer_inventaire,
        name='creer_inventaire'),
    url(r'^objets/inventaires/editer_inventaire/(?P<inventaire_id>\d+)/$',
        views.edit_inventaire, name='editer_inventaire'),
    url(r'^objets/equipements/creer_equipement/$', views.creer_equipement,
        name='creer_equipement'),
    url(r'^objets/equipements/editer_equipement/(?P<equipement_id>\d+)/$',
        views.edit_equipement, name='editer_equipement'),
    url(r'^objets/equipements/editer_equip/(?P<equipement_id>\d+)/$',
        views.edit_equip, name='editer_equip'),
    url(r'^objets/enchantements/creer_enchantement/$', views.creer_enchantement,
        name='creer_enchantement'),
    url(r'^objets/enchantements/editer_enchantement/(?P<enchantement_id>\d+)/$',
        views.edit_enchantement, name='editer_enchantement'),
    url(r'^objets/enchantements/enchantement/(?P<enchantement_id>\d+)/$', views.detail_enchantement,
        name='detail_enchantement'),
    url(r'^objets/enchantements/objets_enchantements/$', views.objets_enchantements,
        name='objets_enchantements'),
    # Quetes
    url(r'^quetes/$', views.quetes, name='quetes'),
    url(r'^quetes/(?P<quete_id>\d+)/$', views.quete, name='quete'),
    url(r'^quetes/reserver_quete_(?P<quete_id>\d+)/$', views.res_quete,
        name='reserver_quete'),
    # RPG
    url(r'^', include('fiches.rpg.avant_garde.urls')),
    url(r'^', include('fiches.rpg.fallout.urls')),
    # Gallery
    url(r'^gallerie/$', views.gallery, name='gallerie'),
    url(r'^gallerie/rechercher/$', views.gallery_search,
        name='rechercher_gallerie'),
    # Campagnes
    url(r'^campagnes/$', views.campagnes, name='campagnes'),
    url(r'^campagnes/(?P<campagne_id>\d+)/$', views.campagne, name='campagne'),
    url(r'^campagnes/(?P<campagne_id>\d+)/(?P<mission_id>\d+)/$', views.mission,
        name='mission'),
    url(r'^campagnes/creer_mission/(?P<campagne_id>\d+)/$', views.creer_mission, name='creer_mission'),
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
    # Conseil
    url(r'^conseil/$', views.conseil, name='conseil'),
    url(r'^conseil/en_cours/$', views.conseil_en_cours, name='conseil_en_cours'),
    url(r'^conseil/editer_notes/$', views.edit_legende,
        name='editer_legende'),
    url(r'^conseil/get_id/(?P<token>\w+)$', views.get_id,
        name='get_id'),
    url(r'^conseil/delete_token/(?P<token>\w+)$', views.delete_token,
        name='delete_token'),
    # Utils
    url(r'^compter_boutiques/$', views.compter_boutiques, name='boutiques'),
    # Autocomplete
    url(r'^fiche-autocomplete/$', views.FicheAutocomplete.as_view(),
        name='fiche-autocomplete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
