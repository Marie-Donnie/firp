from django.conf.urls import include, url
from django.contrib import admin
from fiches import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'firp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^', include('django.contrib.auth.urls')),
    url(r'^fiches/(?P<fiche_id>\d+)/$', views.detailFiche, name='detail'),
    url(r'^creer/$', views.creerfiche),
    url(r'^$', views.index, name='index'),
    url(r'^users/inscription$', views.inscription)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
