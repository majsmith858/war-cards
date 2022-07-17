from django.urls import path

from . import views
from war.views import index, generate_deck

urlpatterns = [
    path('', index, name='index'),
    path('shuffle-deck/', generate_deck, name='shuffle-deck'),
]