import requests
import json

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
