from django.conf.urls import url
from fiches.models import Fiche
from fiches.forms import FicheForm
from fiches.rpg.fallout import views


urlpatterns = [
    # General
    url(r'^fallout/$', views.index, name='fallout'),
]
