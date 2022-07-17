from django.shortcuts import render
from war.models import Player
from war.services import draw_card, get_new_deck
from django.http.response import HttpResponseRedirect
from django.urls import reverse

#This is the index page
def index(request):
    return render(request,'war/index.html')


def generate_deck(request):
    """
    This function generates a deck of cards, shuffles it, and returns the deck.
    
    :param request: The request object
    """
    player_1_cards = get_new_deck()
    player_2_cards = get_new_deck()
    
    return HttpResponseRedirect(reverse("play-game", args=[player_1_cards,player_2_cards]))
