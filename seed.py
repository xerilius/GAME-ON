"""Utility file to seed gaming database DIRECTLY from IGDB API requests"""
from pprint import pprint
from datetime import date
from sqlalchemy import func
from model import connect_to_db, db, Game , Mode, Genre, Theme
from server import app


from api_data import get_game_data
import json

data = get_game_data()
# pprint(data)

def load_games(api_data):
    """Transferring data into database"""
    print("Games")
    
    # store json values into temporary dictionary before transferring into DB 
    game_info = {
        'game_id': None,
       'genres': [],
        'themes': [],
        'slug': None,
        'name': None, 
        'game_mode': []
    }
    

    for json_dict in api_data:
        # game = whole jsonfile
        # print(game.keys()) >> ['id, aggregates, ..']

        # check if genres exist for game and add it to game info dictionary
        if 'genres' in json_dict.keys():
            for i in range(len(json_dict['genres'])):
                genre = json_dict['genres'][i]['name']
                game_info['genres'].append(genre)

        # add themes values to game_info dictionary
        if 'themes' in json_dict.keys():
            for i in range(len(json_dict['themes'])):
                theme = json_dict['themes'][i]['name']
                game_info['themes'].append(theme)

        # add game id to dictionary
        if 'id' in json_dict.keys():
            igdb_id = json_dict['id']
            game_info['game_id'] = igdb_id 

        # add game mode to dictionary
        game_mode = json_dict['game_modes'][0]['name']
        game_info['game_mode'] = game_mode
        # game_mode = game['game_modes'] >> [ {id:2, 'name': Multiplayer'] 
        
        # adding game name to dictionary
        name = json_dict['name']
        game_info['name'] = name

        # Add slug to dictionary
        slug = json_dict['slug']
        game_info['slug'] = slug

        
        # variables to add to game table
        game = Game(igdb_id=game_info['game_id'], game_name=game_info['name'], 
            slug=game_info['slug'])  

        # variable to add to modes table
        mode = Mode(game_mode=game_info['game_mode'])

        # variable to add to theme table
        theme = Theme(theme=game_info['themes'])

        # variable to add to genre table
        genre = Genre(genre=game_info['genres'])


            
        # Add to session or it won't be stored via .bulk_save_objects() for multi arguments
        db.session.add(game)
        db.session.add(theme)
        db.session.add(genre)
        db.session.add(mode)
        # db.session.bulk_save_objects([game, theme, genre, mode])

    # Once done adding data to table, commit work to save progress
    db.session.commit()

 ################## ADD LATER ###########################
        # if 'artworks.url' in json_dict.keys():
        #     for i in range(len(json_dict['artworks.url'])):
        #         artworks = json_dict['artworks'][i]['url']
       
        # if 'collection' in json_dict.keys():
        #     collection = json_dict['collection']['name']
            
        # if 'franchise' in json_dict.keys():
        #     franchise = json_dict['franchise']['name']


        # if 'similar_games' in json_dict.keys():
        #     for i in range(len(json_dict['similar_games'])):
        #         similar_games = json_dict['similar_games'][i]['name']
        #         smlr_game_id = json_dict['themes'][i]['id']
        
        # rating = 
        # rating_count = 
        # screenshots =
     

        # popularity = json_dict['popularity']
        # game_info['popularity'] = popularity
        # release_date = json_dict['release_dates'][0]['human']

        # summary = json_dict['summary']
##########################################################
if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them via database connection (connect_to_db(app))
    db.create_all()
    # Call functions to import different types of data
    load_games(data)




#####################################################################

    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy

     #git add -A instead of * 