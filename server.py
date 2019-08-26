"""Game Reviews and Ratings"""

from jinja2 import StrictUndefined
import os
from datetime import date

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
    games = Game.query.order_by('game_id').limit(10).all()

    return render_template("homepage.html", games=games)

############################## LOGIN
# @app.route('/login', methods=["GET"])
# def show_login():
#     """Displays login form"""
#     return render_template("homepage.html")


@app.route('/login', methods=["POST"])
def login_process():
#     """Redirects user to homepage after login message"""

    username = request.form.get("username")
    password = request.form.get("password")
    # Login form is case sensitive - automatically capitalize username
    username=username.title()

    # query for username in database( returns Truthly/False (none))
    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        flash(username)
        return redirect('/')

    session['Username'] = user.username
    flash("Welcome back, " + session['Username'] + "!")
    return redirect('/')

@app.route('/logout')
def logout():
    """Logs out user"""
    del session['Username']
    flash("Signed out")
    return redirect('/')


######################### REGISTRATION
@app.route('/register', methods=["GET"])
def show_registration_form():
    """Displays registration form"""
    return render_template("registration_form.html")


@app.route('/register', methods=["POST"])
def registration_process():
    """Stores user's registration data in db and returns to homepage"""
    # Grab data from registration form
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('pwd')

    if User.query.filter(User.email == email).first():
        # If email exists in db
        flash("Email already exists.")
        return redirect('/register')

    # Add current date for user sign-up date
    current_date = date.today()
    register_date = current_date.strftime("%Y-%b-%d")
    # Add and commits user's email and password into the DB
    db.session.add(User(username=username.title(), email=email.lower(), password=password, register_date=register_date))
    db.session.commit()
    return redirect('/')

######################################## GAMES

@app.route('/games')
def show_games_list():
    """Show list of games"""
    games = Game.query.order_by('title').all()

    return render_template("games_list.html", games=games)

@app.route('/games/<slug>')
def show_game_details(slug):
    """Display details of each game"""
    game_object = db.session.query(Game).filter(Game.slug==slug).first()
    return render_template('game_details.html', game_object=game_object)

################################### USERS
@app.route('/profile/<username>')
def user_profile(username):
    """Shows user profile"""

    user = User.query.get(username)
    return render_template("user_profile.html", user=user)

@app.route('/terms-of-service', methods=["GET"])
def show_terms_of_service():
    """Displays terms of service"""
    return render_template("terms_of_service.html")

@app.route('/about-me')
def show_about_me_page():
    #react cards
    pass


if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
