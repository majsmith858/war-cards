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

def get_digit_value(value):
    """
    This function converts the value of Jack, Queen, King and Ace to the digit weighting
    :param value: The value to be converted to a digit
    """
    if value == 'JACK':
        value=11
    elif value == "QUEEN":
        value=12
    elif value == "KING":
        value=13
    elif value == "ACE":
        value=14
    return value

def save_score(identity):
    """
    This function saves the score of the player.
    
    :param identity: The identity of the player
    """
    player = Player.objects.get(identity=identity)
    player.score += 1
    player.save()

def calculate_score(request,player_1_deck, player_2_deck, player_1_card, player_2_card):
    """
    This function calculates the score for each players
    
    :param request: the request object
    :param player_1_deck: The deck of the first player
    :param player_2_deck: The deck of the second player
    :param player_1_card: The card that player 1 played
    :param player_2_card: The card that player 2 played
    """
    value_1=get_digit_value(player_1_card)
    value_2=get_digit_value(player_2_card)
    
    if int(value_1) > int(value_2):
        identity="Player 1"
        save_score(identity)
    elif int(value_2) > int(value_1):
        identity="Player 2"
        save_score(identity)
        
    return HttpResponseRedirect(reverse("play-game", args=[player_1_deck,player_2_deck]))
    
def get_winner(players,score=0):
    """
    This function gets the winner of the game
    
    :param players: a list of player objects
    :param score: the score that the players are trying to reach, defaults to 0 (optional)
    """
    for player in players:
        if score == 0:
            score = player.score
            winner = {'Winner':player.identity, 'Score':player.score}
        
        if player.score > score:
            score = player.score
            winner ={'Winner':player.identity, 'Score':player.score}
    return winner

def play_game(request, player_1_deck, player_2_deck):
    """
    It takes in a request and two decks of cards and plays a game of war.
    
    :param request: the request object
    :param player_1_deck: A list of card objects that represent the first player's deck
    :param player_2_deck: A list of card objects that represent the second player's deck
    """
    template_name='war/play.html'
    game_over=False
    players = Player.objects.all()
        
    player_1_draw = draw_card(player_1_deck)
    player_2_draw = draw_card(player_2_deck)
        
    if not (player_1_draw or player_1_draw):
        game_over=True
        winner = get_winner(players)

        context = {'winner':winner, 'game_over':game_over}
    else:
        context = {"players":players, "player_1_draw":player_1_draw[0],
                "player_2_draw":player_2_draw[0],'player_1_deck':player_1_deck,
                'player_2_deck':player_2_deck, 'game_over':game_over}  
        
    return render(request, template_name, context=context)

def clear_score(request):
    """
    It clears the score of the players when the game is over.
    
    :param request: The request object
    """
    players = Player.objects.all()
    for player in players:
        player.score = 0
        player.save()
    return HttpResponseRedirect(reverse("shuffle-deck"))