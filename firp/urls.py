from django.conf.urls import include, url
from django.contrib import admin
from fiches import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'firp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url('^', include('django.contrib.auth.urls')),
    url(r'^login/$', views.authen, name='login'),
    # url(r'^logout/$', name='logout'),
    # url(r'^password_change/$', name='password_change'),
    # url(r'^password_change/done/$', name='password_change_done'),
    url(r'^password_reset/$', views.password_reset, name='password_reset'),
    # url(r'^password_reset/done/$', name='password_reset_done'),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', name='password_reset_confirm'),
    # url(r'^reset/done/$', name='password_reset_complete'),
    url(r'^fiches/(?P<fiche_id>\d+)/$', views.detailFiche, name='detail'),
    url(r'^creer/$', views.creerfiche),
    url(r'^enregistrer/$', views.register),
    url(r'^$', views.index, name='index'),
    url(r'^users/informations$', views.edit_user)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
