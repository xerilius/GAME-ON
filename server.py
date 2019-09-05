"""Game Reviews and Ratings"""

from jinja2 import StrictUndefined
import os
from datetime import date

import json

from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Game, User, Review, Rating, GameMode, Mode
from seed import create_game_json
from api_data import search_game_by_name


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
    # All game info (game_id, slug, title, popularity) filtered by game's slug
    game_object = db.session.query(Game).filter(Game.slug==slug).first()
    # All game reviews for the game specified by game id in reviews table
    reviews = db.session.query(Review).filter(Review.game_id==game_object.game_id).all()

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

    # get user's review
    review = request.form.get('ureview')

    # Get game id
    game_object = db.session.query(Game).filter(Game.slug==slug).first()
    game_id = game_object.game_id
    # store review date
    current_date = date.today()
    review_date = current_date.strftime("%Y-%b-%d")

    # if button pressed to submit game review
    if request.method =='POST':
        print("User attempting to submit review")

        username = session['Username']
        user = User.query.filter_by(username=username).first()
        user_id = user.user_id

        # check if user has already reviewed specified game
        check_review_exists = db.session.query(Review).filter(Review.game_id==game_id,
                                        Review.user_id==user_id).first()
        print(check_review_exists)
        if check_review_exists:
            flash("You have already reviewed this game!")
        # if user has not reviewed game - add review to database:
        if check_review_exists == None:
            db.session.add(Review(game_id=game_id, review=review, user_id=user_id,
                                    review_date=review_date))
            db.session.commit()

    return render_template('game_details.html', game_object=game_object,
                            ss_artworks=ss_artworks, reviews=reviews)


@app.route('/games/search-results', methods=["POST"])
def search_games():
    """Search for games in database and stores new games in db"""
    # get game title from search bar
    game_search = request.form.get("searchbar")
    # query in db to see if game title exists
    search = "%{}%".format(game_search).title()
    game_names = Game.query.filter(Game.title.ilike(search)).all()
    print(game_names)

    if game_names:
            return render_template('search_results.html', games=game_names)

    else:
        # call api_data function to request data from API
        game_request = search_game_by_name(game_search)
        for game_data in game_request:
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
                    mode = Mode.query.filter(Mode.game_mode==mode_name).first()
                    if mode:
                        game.game_modes.append(mode)

            db.session.add(game)
            db.session.commit()
            print(f'Created {game}!')
        return render_template('search_results.html', games=game_names)





    # return render_template('search_results.html', games=[])

####################### Adding Reviews
# @app.route('/reviews/<review_id>/add', methods=["POST"])
# def add_review:(review_id):
#     if not session['Username']:
#         return("Not logged in", 403)
####################### Edit Reviews
# @app.route('/reviews/<review_id>/edit', methods=["POST"])
# def edit_review(review_id):
#     if not session['Username']:
#         return("not logged in",403)
####################### Removing Reviews
@app.route('/reviews/<review_id>/delete', methods=["POST"])
def delete_review(review_id):
        if not session['Username']:
            # (message, status code)
            return("Not logged in", 403)

        username = session['Username']
        user = User.query.filter_by(username=username).first()
        user_id = user.user_id
        print("user_id", user_id)
        print(review_id)

        # review_id is string atm so convert to int
        db.session.delete(Review.query.get(int(review_id)))
        db.session.commit()

        # returning status code
        return("", 204)


################################### USERS
@app.route('/profile/<username>')
def user_profile(username):
    """Shows user profile"""

    user = User.query.get(username)
    return render_template("user_profile.html", user=user)


@app.route('/terms-of-service')
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
