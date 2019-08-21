"""Utility file that makes requests to IGDB API"""

from pprint import pprint
import os
# makes json file more readable
import json
# Allows you to make requests to API
import requests
####################################################################
# To get API key from secret.sh
API_KEY = os.environ.get('IGDB_KEY')
URL = 'https://api-v3.igdb.com/games'
# Add this as a user-key parameter to your API calls to authenticate
headers= {'user-key': API_KEY, 'Accept': 'application/json'}


def get_game_data_w_offset(offset=0):
    """Game data from API requests."""
#######################################
# >>>>> change limit values

    payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"   
           "rating, rating_count, release_dates.human, screenshots.url,"
           "similar_games.name, slug, summary, themes.name;"      
           "limit 5; s popularity desc; w (platforms = [6]);"
           "w themes != (42); offset {};".format(offset))
    
    r = requests.post(URL, headers=headers, data=payload)

    # storing JSON response within variable
    # use request.json() to convert data , data = reponse.json() ???????????
    game_data = json.loads(r.text)

    return(game_data)


def get_game_data():
    """Game data from API requests."""
#######################################
# >>>>> change limit values
    offsets = [0, 50, 100, 150]

    for offset in offsets:

        # get game data
        payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"   
               "rating, rating_count, release_dates.human, screenshots.url,"
               "similar_games.name, slug, summary, themes.name;"      
               "limit 5; s popularity desc; w release_dates.platform = 6;"
               "w themes != (42); offset {};".format(offset))
        
        r = requests.post(URL, headers=headers, data=payload)

        # storing JSON response within variable
        # use request.json() to convert data , data = reponse.json() ???????????
        game_data = json.loads(r.text)

        return(game_data)

# get_game_data()


def get_game_by_id(game_ids):
    pass
    # for game in game_ids:
    #     ",".join(game)

    # game_id_cvs = ",".join(f'{id}' for id in game_ids)

    # payload = ("f name, artworks, slug, genres.name, similar_games.name, status," 
    #            "slug, parent_game, age_ratings, popularity, rating, aggregated_rating, collection.name,rating_count, aggregated_rating_count," 
    #            "first_release_date, storyline, summary, themes.name;" 
    #            "limit 1; w id = ({}); w release_dates.platform = 6; w themes != (42);".format(game_id_cvs))
    # # .get() method which makes GET request and return jspon response-uses params keyword
    # # .post() method which makes POST request - uses data keyword
    # print(payload)

    # response = requests.post(URL, headers=headers, data=payload)
    # data = response.json()
    # print(response.text)

