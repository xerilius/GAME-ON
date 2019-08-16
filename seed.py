"""Utility file to seed gaming database from IGDB API requests"""
from datetime import date
from sqlalchemy import func
from model import connect_to_db, db, Game
from server import app
# from model import Rating
# from model import User

from api_data import get_game_data
import json

data = get_game_data()

def load_games(api_data):
    """Transferring data into database"""
    print("Games")
    
    
    game_info = []

    for json_dict in api_data:
        # game = whole jsonfile
        # print(game.keys()) >> ['id, aggregates, ..']

        if 'artworks.url' in json_dict.keys():
            for i in range(len(json_dict['artworks.url'])):
                artworks = json_dict['artworks'][i]['url']
       
        if 'collection' in json_dict.keys():
            collection = json_dict['collection']['name']
            
        if 'franchise' in json_dict.keys():
            franchise = json_dict['franchise']['name']

        if 'genres' in json_dict.keys():
            for i in range(len(json_dict['genres'])):
                genre = json_dict['genres'][i]['name']

        if 'similar_games' in json_dict.keys():
            for i in range(len(json_dict['similar_games'])):
                similar_games = json_dict['similar_games'][i]['name']
                smlr_game_id = json_dict['themes'][i]['id']

        if 'themes' in json_dict.keys():
            for i in range(len(json_dict['themes'])):
                theme = json_dict['themes'][i]['name']
                
        # rating = 
        # rating_count = 
        # screenshots =
        game_mode = json_dict['game_modes'][0]['name']
        # game_mode = game['game_modes'] >> [ {id:2, 'name': Multiplayer'] ]
        igdb_id = json_dict['id']
        name = json_dict['name']
        popularity = json_dict['popularity']
        release_date = json_dict['release_dates'][0]['human']
        slug = json_dict['slug']
        summary = json_dict['summary']


        game = Game(game_id=igdb_id, title=name, slug=slug,
                    genre=genre, game_mode=game_mode, theme=theme, 
                    summary=summary, release_date=release_date, popularity=popularity,
                    similar_game=similar_game, collection=collection, franchise=franchise,
                    artwork=artwork)

        # Add to session or it won't be stored
        db.session.add(game)

    # Once done adding data to table, commit work to save progress
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them via database connection (connect_to_db(app))
    db.create_all()
    # Call functions to import different types of data
    load_games(data)






    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy