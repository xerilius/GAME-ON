from pprint import pformat
import os

# from jinja2 import StrictUndefined
import requests

from flask import Flask, render_template, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db

app = Flask(__name__)

# Req'd to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# Raises error when silent error caused by undefined variable in Jinja2 
# app.jinja_env.undefined = StrictUndefined

####################################################################
# To get API key from secret.sh
API_KEY = os.environ.get('IGDB_KEY')
# Add this as a user-key parameter to your API calls to authenticate.
URL = 'https://api-v3.igdb.com/games'

headers= {'user-key': API_KEY, 'Accept': 'application/json'}
payload = 'fields genres,url,name;'
# .get() method which makes GET request and return jspon response-uses params keyword
# .post() method which makes POST request - uses data keyword
response = requests.post(URL, headers=headers, data=payload)
data = response.json()

# print(response.text)


# converst data from JSON to python dictionary
# use request.json() to convert data - data = reponse.json()

##################################################################

def loop_thru_data():
# loop over all the values 
    for game in data:
        print(game)

# and print it(replace with insert statement) with sql alchemy

# offset to get the next set



if __name == '__main__':

    # To activate debugger toolbar
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbar(app)

    app.run(host='0.0.0.0')

    # step1 : create  flask requests to API
    # step2 : install all modules required (ex)pip3 install requests) 
    #           via GitBash
    # step3 : pip3 freeze > requirements.txt
    # step4 : make model tables
    # step5 : parse data and insert with sql alchemy