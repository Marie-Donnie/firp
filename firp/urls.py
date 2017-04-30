from django.conf.urls import include, url
from django.contrib import admin
from fiches import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'firp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<fiche_id>\d+)/$', views.detailFiche, name='detail'),
    url(r'^creer/$', views.creerfiche),
    url(r'^$', views.index, name='index'),
]
