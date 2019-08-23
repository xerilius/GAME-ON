"""Game Reviews and Ratings"""

from jinja2 import StrictUndefined
import os
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Game, User, Review, Rating, GameMode, Mode


app = Flask(__name__)
  
# set a 'SECRET_KEY' to enable the Flask session cookies
# app.config['SECRET_KEY'] = '<replace with a secret key>'
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
# This raises an error for silent error caused by undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage"""
    return render_template("homepage.html")

############################## LOGIN
@app.route('/login', methods=["GET"])
def show_login():
    """Displays login form"""
    return render_template("login_form.html")


@app.route('/login', methods=["POST"])
def login_process():
#     """Redirects user to homepage after login message"""
    pass
#     username = request.form.get("email")
#     password = request.form.get("password") 

#     # query for username in database( returns Truthly/False (none))
#     username = db.session.query(User).filter(User.username=username,
#                                         User.password=password).first().username

#     # check if username matches password
#     if username:
#         # log user in - add username from db to 
#         flash("Successfully logged in")
#         session["User"] = username
#         return redirect(f'/users/{user_id}')
#     else:
#         flash("Username/Password is invalid")
#         return redirect("/")

######################### REGISTRATION
@app.route('/register', methods=["GET"])
def show_registration_form():
    """Displays registration form"""
    return render_template("registration_form.html")


@app.route('/register', methods=["POST"])
def registration_process():
    """Stores user's registration data in db and returns to homepage"""
    return redirect('/')


@app.route('/terms-of-service', methods=["GET"])
def show_terms_of_service():
    """Displays terms of service"""
    return render_template("terms_of_service.html")

######################################## GAMES 
@app.route('/games', methods=["GET"])
def show_games_list():
    """Displays games list"""
    return render_template("games_list.html")


if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")