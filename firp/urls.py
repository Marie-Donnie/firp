from django.conf.urls import include, url
from django.contrib import admin
from fiches import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # General
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^login/$', views.login_authen, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    # url(r'^password_change/$', name='password_change'),
    # url(r'^password_change/done/$', name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', name='password_reset_confirm'),
    # url(r'^reset/done/$', name='password_reset_complete'),
    url(r'^enregistrer/$', views.register_user, name='enregistrer'),
    # Users
    url(r'^utilisateurs/$', views.users),
    url(r'^utilisateurs/editer_utilisateur/$', views.edit_user,
        name='editer_utilisateur'),
    url(r'^utilisateurs/creer_profil/$', views.add_profile,
        name='creer_profil'),
    url(r'^utilisateurs/(?P<user_id>\d+)/$', views.aff_user,
        name='utilisateur'),
    # Fiches
    url(r'^personnages/$', views.personnages),
    url(r'^fiches/(?P<fiche_id>\d+)/$', views.detail_fiche,
        name='detail_fiche'),
    url(r'^fiches/editer_fiche/(?P<fiche_id>\d+)/$', views.edit_fiche,
        name='editer_fiche'),
    url(r'^creer/$', views.creer_fiche, name='creer_fiche')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
