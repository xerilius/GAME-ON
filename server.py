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

############################## Login routes
@app.route('/login', methods=["GET"])
def display_login():
    """Displays login form"""
    return render_template("login_form.html")


# @app.route('/login', methods=["POST"])
# def login_process():
#     """Redirects user to homepage after login message"""
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

@app.route('/register', methods=["POST"])
def show_register_form():
    """Displays registration form"""
    return render_template("registration_form.html")


if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")