"""fdgforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.http import last_modified
from django.views.i18n import JavaScriptCatalog

from misago.users.forms.auth import AdminAuthenticationForm

from fiches import views

admin.autodiscover()
admin.site.login_form = AdminAuthenticationForm


urlpatterns = [
    url(r'^', include('misago.urls', namespace='misago')),

    # Javascript translations
    url(
        r'^django-i18n.js$',
        cache_page(86400 * 2, key_prefix='misagojsi18n')(
            last_modified(lambda req, **kw: timezone.now())(
                JavaScriptCatalog.as_view(
                    packages=['misago'],
                ),
            ),
        ),
        name='django-i18n'
    ),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index$', views.index, name='index'),
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
    # Quetes
    url(r'^quetes/$', views.quetes, name='quetes'),
    url(r'^quetes/(?P<quete_id>\d+)/$', views.quete, name='quete'),
    # RPG
    url(r'^', include('fiches.rpg.avant_garde.urls')),

    # Uncomment next line if you plan to use Django admin for 3rd party apps
    url(r'^django-admin/', admin.site.urls),
]


# If debug mode is enabled, include debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]


# Use static file server for static and media files (debug only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Error Handlers
# Misago needs those handlers to deal with errors raised by it's middlewares
# If you replace those handlers with custom ones, make sure you decorate them
# with shared_403_exception_handler or shared_404_exception_handler
# decorators that are defined in misago.views.errorpages module!
handler403 = 'misago.core.errorpages.permission_denied'
handler404 = 'misago.core.errorpages.page_not_found'
