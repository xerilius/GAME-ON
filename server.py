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
        flash("Invalid Username/Password")

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
    username = request.form.get('username').title()
    email = request.form.get('email')
    password = request.form.get('pwd')

    # Check if username exists in db
    if User.query.filter(User.username == username).first():
        flash("Username already exists.")
        return redirect('/register')

    # Check if email exists in db
    if User.query.filter(User.email == email).first():
        flash("Email already exists.")
        return redirect('/register')

    # Add current date for user sign-up date
    else:
        current_date = date.today()
        register_date = current_date.strftime("%Y-%b-%d")
        # Add and commits user's email and password into the DB
        db.session.add(User(username=username, email=email.lower(), password=password, register_date=register_date))
        db.session.commit()

    return redirect('/')

######################################## GAMES
@app.route('/games')
def show_games_list():
    """Show list of games"""
    games = Game.query.order_by('title').all()

    return render_template("games_list.html", games=games)


@app.route('/games/<slug>', methods=["GET", "POST"])
def show_game_details(slug):
    """Display details of each game"""
    game_object = db.session.query(Game).filter(Game.slug==slug).first()

    # stores screenshots AND artworks
    ss_artworks = []
    # modify url to get original images of screenshots instead of thumbnails
    for url in game_object.screenshot_urls:
        # obtain each component of url
        replace_var = url.split('/')
        # join result of modification via slicing and concatenation
        newurl = ('/').join(replace_var[:-2] + ['t_original'] + replace_var[-1:])
        # save modified url to list
        ss_artworks.append(newurl)

    # modify url to get original images of artwork instead of thumbnails
    for url in game_object.artwork_urls:
        replace_ = url.split('/')
        newurl = ('/').join(replace_[:-2] + ['t_original'] + replace_[-1:])
        ss_artworks.append(newurl)


        # return reviews and ratings
    return render_template('game_details.html', game_object=game_object,
                            ss_artworks=ss_artworks)

@app.route('/games/<slug>', methods=["POST"])
def get_game_reviews(slug):
    """Stores user game review into database to display on page"""
    # Get review data
    review = request.form.get('ureview')
    # Get username

    username = session['Username']
    user = User.query.filter_by(username=username).first()
    user_id = user.user_id
    # Get game id
    game_object = db.session.query(Game).filter(Game.slug==slug).first()
    game_id = game_object.game_id

    current_date = date.today()
    review_date = current_date.strftime("%Y-%b-%d")

    db.session.add(Review(game_id=game_id, review=review, user_id=user_id,review_date=review_date))
    db.session.commit()

    return redirect('/games/<slug>')



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
