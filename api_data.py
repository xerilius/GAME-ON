from pprint import pprint
import os
# makes json file more readable
import json
# allows you to make requests to API
import requests

from model import connect_to_db, db

####################################################################
# To get API key from secret.sh
API_KEY = os.environ.get('IGDB_KEY')
URL = 'https://api-v3.igdb.com/games'
# Add this as a user-key parameter to your API calls to authenticate.
headers= {'user-key': API_KEY, 'Accept': 'application/json'}


def test_data():
    """API request for games."""

    offsets = [0]

    for offset in offsets:

        # get game data
        payload = ("f name, artworks.url, slug, franchise.name, collection.name,"
               "game_modes.name, genres.name, similar_games.name," 
               "slug, popularity," 
               "rating, aggregated_rating,"
               "rating_count, aggregated_rating_count," 
               "release_dates.human, storyline, summary, themes.name;" 
               "limit 5; s popularity desc; w release_dates.platform = 6; w themes != (42); offset {};".format(offset))
        
        r = requests.post(URL, headers=headers, data=payload)

        # storing JSON response within variable
        data = json.loads(r.text)
        # pprint(data)

        for json_dict in data:
            # game = whole jsonfile
            # print(game.keys()) >> ['id, aggregates, ..']
           
            if 'collection' in json_dict.keys():
                collection = json_dict['collection']['name']
                
            if 'franchise' in json_dict.keys():
                franchise = json_dict['franchise']['name']
                
            if 'similar_games' in json_dict.keys():
                for i in range(len(json_dict['similar_games'])):
                    similar_games = json_dict['similar_games'][i]['name']

            if 'themes' in json_dict.keys():
                for i in range(len(json_dict['themes'])):
                    theme = json_dict['themes'][i]['name']
                    smlr_game_id = json_dict['themes'][i]['id']
        
            game_mode = json_dict['game_modes'][0]['name']
            # game_mode = game['game_modes'] >> [ {id:2, 'name': Multiplayer'] ]
            igdb_id = json_dict['id']
            name = json_dict['name']
            popularity = json_dict['popularity']
            release_date = json_dict['release_dates'][0]['human']
            slug = json_dict['slug']
            summary = json_dict['summary']


            

        print(name, slug, igdb_id, popularity, release_date, summary, collection,
                franchise, game_mode, theme, smlr_game_id)



            
            

           
            




        # pretty printing json string back
        # game_data = json.dumps(game_dict, indent=4, sort_keys=True)

        
        # for i in range(results):
        #     game_modes = game['gameInfo'][i].get('game_modes')
        #     genres = game['gameInfo'][i].get('genres')
        #     game_id = game['gameInfo'][i].get('id')
        #     name = game['gameInfo'][i].get('name')
        #     popularity =  game['gameInfo'][i].get('popularity')
        #     rating = game['gameInfo'][i].get('rating')
        #     rating_count = game['gameInfo'][i].get('rating_count')
        #     release_dates = game['gameInfo'][i].get('release_dates')
        #     similar_games = game['gameInfo'][i].get('similar_games')
        #     slug = game['gameInfo'][i].get('slug')
        #     summary = game['gameInfo'][i].get('summary')
        #     themes = game['gameInfo'][i].get('themes')

        #     print(results.text)
test_data()

   
        # # create new data_file.json file with write mode 
        # with open('game_data.txt', 'w') as text_file:
        #     # write json data into file
        #     json.dump(game_data, text_file)

# def get_game_by_id(game_ids):

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

# get_game_img()  

def get_developer_info_for_game():
    """API request for game developer info"""
    # url3 = https://api-v3.igdb.com/companies
    # payload = "f name, developed, published, game; w game id"
    pass
def get_age_rating_for_game():
    pass


# convert data from JSON to python dictionary
# use request.json() to convert data , data = reponse.json()

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


