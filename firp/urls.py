from django.conf.urls import include, url
from django.contrib import admin
from fiches import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # General
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    # Users
    url(r'^utilisateurs/$', views.users,
        name='utilisateurs'),
    url(r'^utilisateurs/editer_utilisateur/$', views.edit_user,
        name='editer_utilisateur'),
    url(r'^utilisateurs/gestion_profil/$', views.profile,
        name='gestion_profil'),
    url(r'^utilisateurs/(?P<user_id>\d+)/$', views.aff_user,
        name='utilisateur'),
    # Fiches
    url(r'^personnages/$', views.personnages,
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
        name='creer_inventaire')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
