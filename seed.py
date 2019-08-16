"""Utility file to seed gaming database from IGDB API requests"""

from pprint import pformat
import os

import requests

import datetime
from sqlalchemy import func

from api_data import get_game_data

from model import connect_to_db, db
# from server import appp


def load_games(api_request):
    """Transferring data into database"""
    print("Games")













    # parse thru data 





# if __name__ == '__main__':

    # To activate debugger toolbar
    # app.debug = True

    # connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbar(app)

    # app.run(host='0.0.0.0')

    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy