"""Models and database functions for GameOn Review Site"""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database via Flask-SQLAlchemy to use session

db = SQLAlchemy()

#########################################################################
# Model defintions
class Game(db.Model):
    """Games on gaming website."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    igdb_id = db.Column(db.Integer, unique=True)
    title = db.Column(db.String, nullable=False, unique=True)
    slug = db.Column(db.String, nullable=False, unique=True)

    summary = db.Column(db.String, nullable=True)
    release_date = db.Column(db.Date, nullable=True)
    popularity = db.Column(db.Float, nullable=True)

    artwork_urls = db.Column(db.JSON, nullable=True)
    screenshot_urls = db.Column(db.JSON, nullable=True)

    # similar_games = db.Column(db.String, nullable=False)
    # sim_game_igdb_id = db.Column(db.Integer, unique=True)
    # collection = db.Column(db.String, nullable=True)
    # franchise = db.Column(db.String, nullable=True)

    # Association relationships for modes, genres, themes
    game_modes = db.relationship("Mode", secondary="game_modes", backref="games")
    # genres = db.relationship("Genre", secondary="game_genres", backref="games")
    # themes = db.relationship("Theme", secondary="game_themes", backref="games")


    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Game game_id={} title={} release_date={} popularity={}>".format(
            self.game_id, self.title, self.release_date, self.popularity)


###################################
class Mode(db.Model):
    """Modes for each game"""

    __tablename__ = "modes"
    mode_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_mode = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Mode mode_id={} game_mode={}>".format(
                self.mode_id, self.game_mode)


class GameMode(db.Model):
    """Association table for Game & Mode"""

    __tablename__ =  "game_modes"
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), primary_key=True)
    mode_id = db.Column(db.Integer, db.ForeignKey('modes.mode_id'), primary_key=True)

    def __repr__(self):
        return "<GameMode game_id={} mode_id={}>".format(
                    self.game_id, self.game_mode)

################################################################
class Rating(db.Model):
    """Rating of game by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    rating = db.Column(db.Integer, nullable=True)

    # Define relationship to User
    user = db.relationship('User', backref=db.backref('ratings',
                                                      order_by=rating_id))
    # Define relationship to Game
    game = db.relationship('Game', backref=db.backref('ratings',
                                                      order_by=rating_id))

    def __repr__(self):
        """Provides helpful representation when printed"""

        return "<Rating rating_id={} game_id={} rating={}>".format(
                self.rating_id, self.game_id, self.rating)

################################################################
class Review(db.Model):
    """User reviews"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    review = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    review_date =  db.Column(db.Date, nullable=False)

    # Define relationship to User
    user = db.relationship('User', backref=db.backref('reviews',
                                                      order_by=review_id))
    # Define relationship to Game
    game = db.relationship('Game', backref=db.backref('reviews',
                                                      order_by=review_id))

    def __repr__(self):
        """Provides helpful representation when printed"""

        return "<Review review_id={} game_id={} review={}>".format(
                self.review_id, self.game_id, self.review)

######################################################################
class User(db.Model):
    """User of Gaming website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    register_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        """Provies helpful representation when printed"""

        return "<User user_id={} username={} password={} email={} register_date={}".format(
            self.user_id, self.username, self.password, self.email,
                        self.register_date)
######################

# class Genre(db.Model):
#     """Genre for each game"""

#     __tablename__ = "genres"
#     genre_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     genre = db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return "<Genre genre_id={} genre_name={}>".format(
#         self.genre_id, self.genre_name)


# class GameGenre(db.Model):
#     """Association table for Game & Genre"""
#     __tablename__ = "game_genres"
#     game_id= db.Column(db.Integer, db.ForeignKey('games.game_id'), primary_key=True)
#     genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id'), primary_key=True)

#     def __repr__(self):
#         return"<GameGenre game_id={} genre_id={}>".format(
#             self.game_id, self.genre_id)

# ###########################

# class Theme(db.Model):
#     """Theme of each game """

#     __tablename__ = "themes"
#     theme_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     theme = db.Column(db.String, nullable=False)

#     def __repr__(self):
#         return "<Theme theme_id={} theme_name={}>".format(
#                 self.theme_id, self.theme_name)


# class GameTheme(db.Model):
#     """Association table for Game & Theme"""

#     __tablename__ = "game_themes"
#     game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), primary_key=True)
#     theme_id = db.Column(db.Integer, db.ForeignKey('themes.theme_id'), primary_key=True)

#     def __repr__(self):
#         return "<GameTheme game_id={} theme_id={}>".format(
#                 self.game_id, self.theme_id)


# class Newsfeed(db.Model):
#     """News feed of games """

#     __tablename__ = "news"

#     news_id = db.Column(db.Integer, autoincrement=True, nullable=False)
#     game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
#     text = db.Column(db.String)
#     news_date = db.Column(db.DateTime)

    # Define relationship to Game


# class Favorited(db.Model):
#     """Favorited games."""

#     __tablename__ = "favorites"

#     favorited_id = db.Column(db.Integer, autoincrement=True, nullable=True)
#     game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'))
#     num_likes = db.Column(db.Integer)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    # Define relationship to Game

    # Define relationship to User

#########################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///gameon'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # For convenience. if we run this module interactively,
    # it will leave you in a state of being able to work with
    # the database directly.

    from server import app
    connect_to_db(app)
    print("Connected to GameOn-Line Database")
