from django.urls import path

from . import views
from war.views import index, generate_deck, play_game, calculate_score

urlpatterns = [
    path('', index, name='index'),
    path('shuffle-deck/', generate_deck, name='shuffle-deck'),
    path('play/<str:player_1_deck>/<str:player_2_deck>/', play_game, name='play-game'),
    path('calculate-score/<str:player_1_deck>/<str:player_2_deck>/<str:player_1_card>/<str:player_2_card>/', calculate_score, name='cal-score'),
]