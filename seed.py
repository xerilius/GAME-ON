
"""Utility file to seed gaming database DIRECTLY from IGDB API requests"""

from pprint import pprint
from datetime import datetime
from sqlalchemy import func
from model import connect_to_db, db, Game , Mode
from server import app

from api_data import get_game_data, get_game_data_w_offset
import json

# connect and create db
connect_to_db(app)
db.create_all()

# API request
# data = get_game_data_w_offset()
data = get_game_data()
# pprint(data)

# manually adding modes and adding it to Mode table under game_mode field
single_player = Mode(game_mode='Single player')
multi_player = Mode(game_mode='Multiplayer')
co_op = Mode(game_mode='Co-op')
mmo = Mode(game_mode='MMO')

# add all variables to db
db.session.add_all([single_player, multi_player, co_op, mmo])
db.session.commit()

# hard code game modes for game_mode field in modes table
game_modes = {
    'Single player': single_player,
    'Multiplayer': multi_player,
    'Co-operative': co_op,
    'Massively Multiplayer Online (MMO)': mmo,
}


def create_game_json(json_dict):
    game_info = {
        'artworks': [],
        'game_id': None,
        'name': None, 
        'game_modes': [],
        # 'genres': [],
        'popularity': None,
        'release_date': None,
        'screenshots': [],
        # 'similar_games': [],
        'slug': None,
        'summary': None,
        # 'themes': [],
        # 'rating': None,
        # 'rating_count': None,    
    }
    
    # game = whole jsonfile
    # print(game.keys()) >> ['id, aggregates, ..']

    igdb_id = json_dict['id']
    game_info['game_id'] = igdb_id

    name = json_dict['name']
    game_info['name'] = name.strip()

    slug = json_dict['slug']
    game_info['slug'] = slug.strip()

    # Add popularity of the game to dictionary
    popularity = json_dict['popularity']
    game_info['popularity'] = popularity

    # Add release date of game to dictionary
    
    release_date = json_dict['release_dates'][0]['human']
    game_info['release_date'] = release_date
    
 

    # # Add rating to dictionary
    # if 'rating' in json_dict:
    #     rating = game_info['rating'] 
    #     game_info['rating'] = rating

    # Add summary of game to dictionary
    if 'summary' in json_dict:
        summary = json_dict['summary']
        game_info['summary'] = summary


    # # Checks if genres exist for game and add it to game info dictionary
    # if 'genres' in json_dict:
    #     # loop thru genre's list 
    #     for genre in json_dict['genres']:
    #         genre_name = genre['name']
    #         # store genre to temp dictionary
    #         game_info['genres'].append(genre_name)

    # # Add themes values to game_info dictionary
    # if 'themes' in json_dict:
    #     for theme in json_dict['themes']:
    #         theme_name = theme['name']
    #         game_info['themes'].append(theme)

    # Add game mode to dictionary
    for mode in json_dict['game_modes']:
        print("mode", mode)
        game_mode = mode['name']
        print("game_mode" , game_mode)
        game_info['game_modes'].append(game_mode.strip())
 
    
    # Add list of artworks URL to dictionary list
    if 'artworks' in json_dict:
        for artwork in json_dict['artworks']:
            artwork_url = artwork['url']
            game_info['artworks'].append(artwork_url.strip())

    # Add list of screenshot URLs to dictionary
    if 'screenshots' in json_dict:
        for screenshot in json_dict['screenshots']:
            screenshot_url = screenshot['url']
            game_info['screenshots'].append(screenshot_url.strip())

    # # Add similar games to dictionary list
    # if 'similar_games' in json_dict:
    #     for game in json_dict['similar_games']:
    #         sim_game_id = game['id']
    #         game_info['similar_games'].append(sim_game_id)

    print(game_info)

    return game_info


def load_games(api_data):
    """Transferring data into database"""
    print("Games")

    # Delete all rows in table, so if run this second time,
        # we wont be trying to add duplicate data
    Game.query.delete()

    # store json values into temporary dictionary before transferring into DB
    for game_data in api_data:
        game_info = create_game_json(game_data) 

       
        if game_info['release_date']:
            release_date = datetime.strptime(game_info['release_date'], '%Y-%b-%d').date()
 

        # variables to add to game table
        game = Game(
            igdb_id=game_info['game_id'],
            title=game_info['name'], 
            slug=game_info['slug'],
            artwork_urls=game_info['artworks'], 
            popularity=game_info['popularity'],
            screenshot_urls=game_info['screenshots'],
            release_date=release_date,
            summary=game_info['summary']) 

        for mode_name in game_info['game_modes']:
            mode = game_modes[mode_name]
            game.game_modes.append(mode)

        # #################################################3
        # for genre_name in game_info['genres']:
        #     genre = game_genres[genre_name]
        #     game.game_genres.append(genre)



        db.session.add(game)

        # db.session.add(rating)
        db.session.commit()
        print(f'Created {game}!')
      
    # Once done adding data to table, commit work to save progress
    # db.session.commit()

load_games(data)


#####################################################################

    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy

     #git add -A instead of * 