"""Utility file that makes calls to IGDB API"""

from pprint import pprint
import os
# makes json file more readable
import json
# Allows you to make requests to API
import requests

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
CLIENT_ID = os.environ.get('CLIENT_ID')
URL = 'https://api.igdb.com/v4/games'

# Add this as a Auth parameter to your API calls to authenticate using api key
headers = {
    'Client-ID': CLIENT_ID,
    'Authorization':'Bearer '+ ACCESS_TOKEN, 
    'Accept': 'application/json',
}

def get_game_data_w_offset0():
    payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"
        "rating, rating_count, release_dates.human, screenshots.url,"
        "similar_games.name, slug, summary, themes.name;"
        "limit 5; s popularity desc; w (platforms = [6]);"
           "w themes != (42); offset {};".format(0))
           
    r1 = requests.post(URL, headers=headers, data=payload)
    game_data = json.loads(r1.text)
    print(game_data)
    return game_data

get_game_data_w_offset0()



def get_game_data_w_offset50():
    """Game data from API requests with offset = 50."""

    payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"
        "rating, rating_count, release_dates.human, screenshots.url,"
        "similar_games.name, slug, summary, themes.name;"
        "limit 50; s popularity desc; w (platforms = [6]);"
        "w themes != (42); offset {};".format(50))

    r2 = requests.post(URL, headers=headers, data=payload)
    game_data = json.loads(r2.text)
    return game_data



def get_game_data_w_offset100():
    """Game data from API requests with offset = 100."""

    payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"
        "rating, rating_count, release_dates.human, screenshots.url,"
        "similar_games.name, slug, summary, themes.name;"
        "limit 50; s popularity desc; w (platforms = [6]);"
        "w themes != (42); offset {};".format(100))

    r3 = requests.post(URL, headers=headers, data=payload)
    game_data = json.loads(r3.text)
    return game_data



def get_game_data_w_offset150():
    """Game data from API requests with offset = 150."""

    payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"
           "rating, rating_count, release_dates.human, screenshots.url,"
           "similar_games.name, slug, summary, themes.name;"
           "limit 50; s popularity desc; w (platforms = [6]);"
           "w themes != (42); offset {};".format(150))

    r4 = requests.post(URL, headers=headers, data=payload)
    game_data = json.loads(r4.text)
    return game_data



def search_game_by_name(game_name):
    """Game data from API request filtered by game name"""

    payload = ("f  artworks.url, game_modes.name, genres.name, name, popularity,"
               "rating, rating_count, release_dates.human, screenshots.url,"
               "similar_games.name, slug, summary, themes.name;"
               "limit 50; w (platforms = [6]); search \"{}\";"
               "w themes != (42);".format(game_name))

    r5 = requests.post(URL, headers=headers,data=payload)
    game_data = json.loads(r5.text)
    return game_data



def search_game_by_id(game_ids):
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
