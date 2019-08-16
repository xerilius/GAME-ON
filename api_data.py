"""Utility file that makes requests to IGDB API"""
from pprint import pprint
import os
# makes json file more readable
import json
# allows you to make requests to API
import requests
####################################################################
# To get API key from secret.sh
API_KEY = os.environ.get('IGDB_KEY')
URL = 'https://api-v3.igdb.com/games'
# Add this as a user-key parameter to your API calls to authenticate
headers= {'user-key': API_KEY, 'Accept': 'application/json'}


def get_game_data():
    """Game data from API requests."""
#######################################
# >>>>> change limit values
    offsets = [0, 50, 100, 150]

    for offset in offsets:

        # get game data
        payload = ("f  artworks.url, collection.name, franchise.name, "
               "game_modes.name, genres.name, name, popularity,"   
               "rating, rating_count, release_dates.human, screenshots.url,"
               "similar_games.name, slug, summary, themes.name;"      
               "limit 5; s popularity desc; w release_dates.platform = 6;"
               "w themes != (42); offset {};".format(offset))
        
        r = requests.post(URL, headers=headers, data=payload)

        # storing JSON response within variable
        # use request.json() to convert data , data = reponse.json() ???????????
        game_data = json.loads(r.text)

        return(game_data)

get_game_data()

     # create new data_file.json file with write mode 
        # with open('game_data.txt', 'w') as text_file:
        #     # write json data into file
        #     json.dump(game_data, text_file)

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

def get_game_img():
    pass

def get_developer_info_for_game():
    """API request for game developer info"""
    # url3 = https://api-v3.igdb.com/companies
    # payload = "f name, developed, published, game; w game id"
    pass

def get_age_rating_for_game():
    pass


##################################################################
# and print it(replace with insert statement) with sql alchemy
# offset to get the next set

# Filters: 
    # "f name, genres; where id = 12343;
    #/games/
    # search "zelda"; where rating >=80 & release_dates.date > ;
# sort : "fields *; sort popularity asc/desc"
# sort: "f * ; s popularity asc/desc"
# sort release_dates.date desc; where rating >=90;

# fields: "f name, release_dates, genres.name,rating;"

# where: fields *; where genres = 4; 
# where : "f *; w genres = 4;"
# do fields name, genres.name; where id = 1942;
# f name, release_dates, genres.name,rating; w id = (435,23,143)

# for games :
# search : search "Halo"; fields name; or f name;
# same as:




# if __name == '__main__':

#     # To activate debugger toolbar
#     app.debug = True

#     connect_to_db(app)

#     # Use the DebugToolbar
#     DebugToolbar(app)

#     app.run(host='0.0.0.0')



    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy