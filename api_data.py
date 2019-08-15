from pprint import pprint
import os
import json
import requests

from model import connect_to_db, db

# Raises error when silent error caused by undefined variable in Jinja2 
# app.jinja_env.undefined = StrictUndefined

####################################################################
# To get API key from secret.sh
API_KEY = os.environ.get('IGDB_KEY')
# Add this as a user-key parameter to your API calls to authenticate.
URL = 'https://api-v3.igdb.com/games'

headers= {'user-key': API_KEY, 'Accept': 'application/json'}
payload = "f name, alternative..."


def get_game_by_id(game_ids):

    # for game in game_ids:
    #     ",".join(game)

    game_id_cvs = ",".join(f'{id}' for id in game_ids)

    payload = ("f name, artworks, slug, genres.name, similar_games.name, status," 
               "slug, parent_game, age_ratings, popularity, rating, aggregated_rating, collection.name,rating_count, aggregated_rating_count," 
               "first_release_date, storyline, summary, themes.name;" 
               "limit 1; w id = ({}); w release_dates.platform = 6; w themes != (42);".format(game_id_cvs))
    # .get() method which makes GET request and return jspon response-uses params keyword
    # .post() method which makes POST request - uses data keyword
    print(payload)

    response = requests.post(URL, headers=headers, data=payload)
    data = response.json()
    print(response.text)



def test_data():
    """API request for games."""

    loop_count = 0
    position_num = 0

    while loop_count < 5:

        loop_count += 1

        if loop_count == 2:
            position_num = 50
 
        if loop_count == 3:
            position_num = 100

        if loop_count == 4:
            position_num = 150

        if loop_count == 5:
            position_num = 200

        # if loop_count == 6:
        #     position_num = 250

        # if loop_count == 300:
        #     position_num = 300
    

        payload = ("f name, artworks.url, slug, franchise.name, collection.name,"
               "game_modes.name, genres.name, similar_games.name," 
               "slug, age_ratings, popularity," 
               "rating, aggregated_rating,"
               "rating_count, aggregated_rating_count," 
               "release_dates.human, storyline, summary, themes.name;" 
               "limit 5; s popularity desc; w release_dates.platform = 6; w themes != (42); offset {};".format(position_num))
        
        print(payload)
        print()

        response = requests.post(URL, headers=headers, data=payload)
        data = json.loads(response.text) # data = response.json()



        pprint(data)

        print("game:", loop_count)
        print("position:", position_num)

       
        print("-"*100)
    
test_data()



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


