
"""Utility file to seed gaming database DIRECTLY from IGDB API requests"""

from pprint import pprint
from datetime import datetime
from sqlalchemy import func
from model import connect_to_db, db, Game , Mode

from api_data import get_game_data_w_offset0, get_game_data_w_offset50
from api_data import get_game_data_w_offset100, get_game_data_w_offset150

import json

def create_game_json(json_dict):
    """Temporary dictionary to organize json data before transferred into db"""

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
    if 'release_dates' in json_dict:
        release_date = json_dict['release_dates'][0]['human']
        game_info['release_date'] = release_date
     # Add release date of game to dictionary
    if game_info['release_date']:
        if len(game_info['release_date']) == 3:
            game_info['release_date'] = None
        elif len(game_info['release_date']) <= 7:
            game_info['release_date'] = datetime.strptime(game_info['release_date'][0:4], '%Y')
        elif len(game_info['release_date']) >=10:
            game_info['release_date'] = datetime.strptime(game_info['release_date'], '%Y-%b-%d')
        elif len(game_info['release_date']) == 8:
            game_info['release_date'] = datetime.strptime(game_info['release_date'], '%Y-%b')
        else:
            game_info['release_date'] = None
    # Add summary of game to dictionary
    if 'summary' in json_dict:
        summary = json_dict['summary']
        game_info['summary'] = summary

    # Add game mode to dictionary
    if 'game_modes' in json_dict:
        for mode in json_dict['game_modes']:
            print("mode", mode)
            game_mode = mode['name']
            print("game_mode" , game_mode)
            game_info['game_modes'].append(game_mode)

    # Add list of artworks URL to dictionary list
    if 'artworks' in json_dict:
        for artwork in json_dict['artworks']:
            artwork_url = artwork['url']
            game_info['artworks'].append(artwork_url)

    # Add list of screenshot URLs to dictionary
    if 'screenshots' in json_dict:
        for screenshot in json_dict['screenshots']:
            screenshot_url = screenshot['url']
            game_info['screenshots'].append(screenshot_url)

    # # Add similar games to dictionary list
    # if 'similar_games' in json_dict:
    #     for game in json_dict['similar_games']:
    #         sim_game_id = game['id']
    #         game_info['similar_games'].append(sim_game_id)

    print(game_info)
    return game_info


def load_games(api_data, game_modes):
    """Transferring game data into database"""
    print("Games")

    # store json values into temporary dictionary before transferring into DB
    for game_data in api_data:
        game_info = create_game_json(game_data)
        # variables to add to game table
        game = Game(
            igdb_id=game_info['game_id'],
            title=game_info['name'],
            slug=game_info['slug'],
            artwork_urls=game_info['artworks'],
            popularity=game_info['popularity'],
            screenshot_urls=game_info['screenshots'],
            release_date=game_info['release_date'],
            summary=game_info['summary'])

        if game_info['game_modes']:
            for mode_name in game_info['game_modes']:
                mode = game_modes[mode_name]
                game.game_modes.append(mode)

        # #################################################3
        # for genre_name in game_info['genres']:
        #     genre = game_genres[genre_name]
        #     game.game_genres.append(genre)

        db.session.add(game)
        db.session.commit()
        print(f'Created {game}!')



if __name__ == '__main__':
    from server import app
    # connect and create db
    connect_to_db(app)
    db.create_all()

    # API request
    data1 = get_game_data_w_offset0()
    data2 = get_game_data_w_offset50()
    data3 = get_game_data_w_offset100()
    data4 = get_game_data_w_offset150()
    # pprint(data)

    # manually adding modes and adding it to Mode table under game_mode field
    single_player = Mode(game_mode='Single player')
    multi_player = Mode(game_mode='Multiplayer')
    co_op = Mode(game_mode='Co-op')
    mmo = Mode(game_mode='MMO')
    split_screen = Mode(game_mode='Split screen')
    # add all variables to db
    db.session.add_all([single_player, multi_player, co_op, mmo, split_screen])
    db.session.commit()
    # hard code game modes for game_mode field in modes table
    game_modes = {
        'Single player': single_player,
        'Multiplayer': multi_player,
        'Co-operative': co_op,
        'Massively Multiplayer Online (MMO)': mmo,
        'Split screen': split_screen
    }

    load_games(data1, game_modes)
    load_games(data2, game_modes)
    load_games(data3, game_modes)
    load_games(data4, game_modes)
