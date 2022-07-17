import requests
import json
from requests.exceptions import Timeout

def get_api(url,params,timeout=10):
    """
    This function is used to make an api call
    
    :param url: The URL of the API endpoint
    :param params: a dictionary of parameters to be sent to the API
    :param timeout: The time to wait for the server to send data before timing out
    """
    try:
        req = requests.get(url, params=params, timeout=timeout)
    except Timeout:
        print('Timeout has been raised.')
    return req

def get_new_deck():
    """
    This function creates a new deck of cards.
    """
    url = 'https://deckofcardsapi.com/api/deck/new/shuffle/'
    param = {'deck_count':1}
    
    req = get_api(url, param)
    deck=json.loads(req.text)
    return deck['deck_id']

def draw_card(deck_id):
    """
    It draws a card from the deck.
    
    :param deck_id: The deck_id is the unique identifier for the deck you want to draw from
    """
    url = f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/'
    param = {'count':1}
    req = get_api(url, param)

    card=json.loads(req.text)
    return card['cards']