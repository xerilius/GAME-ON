"""Models and database functions"""
from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database via Flask-SQLAlchemy to use session

db = SQLAlchemy()

# Model defintions

class Game(db.Model):
    """Games on gaming website."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    slug = db.Column(db.String, nullable=False)

    genre = db.Column(db.String, nullable=False)
    themes = db.Column(db.String, nullable = False, unique=True)
    summary = db.Column(db.String, nullable=False)
    storyline = db.Column(db.String, nullable=True)
    release_date = db.Column(db.DateTime, nullable=False)
    popularity = db.Column(db.Integer, nullable=True)

    similar_game = db.Column(db.String, nullable=False)
    collection_name = db.Column(db.String, nullable=False)
    franchise = db.Column(db.String, nullable=False)
    
    game_mode = db.Column(db.String(20), nullable=False)
        
    # artwork = db.Column(db.String, nullable=True)
    # screenshot = db.Column(db.String, nullable=True)
    # developer = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Game game_id={} title={} genre={} release_date={} game_mode={} popularity={}>".format(
            self.game_id, self.title, self.genre,
                        self.description, self.release_date)

# class GameMetadata(db.Model):
#     """Metadata for game"""


class Rating(db.Model):
    """Rating of game by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.games_id'), nullable=False)
    star_rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    rating = db.Column(db.Integer, nullable=True)
    aggregated_rating = db.Column(db.Integer, nullable=True)

    rating_count = db.Column(db.Integer, nullable=True)
    aggregated_rating_count = db.Column(db.Integer, nullable=True)

    # Define relationship to User
    user = db.relationship('User', backref=db.backref('ratings',
                                                      order_by=rating_id))
    # Define relationship to Game
    game = db.relationship('Game', backref=db.backref('ratings',
                                                      order_by=rating_id))

    def __repr__(self):
        """Provides helpful representation when printed"""

        return "<Rating rating_id={} game_id={} star_rating={}>".format(
                self.rating_id, self.game_id, self.star_rating)


class Review(db.Model):
    """User reviews"""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False)
    review = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)

    # Define relationship to User
    user = db.relationship('User', backref=db.backref('reviews',
                                                      order_by=review_id))
    # Define relationship to Game
    game = db.relationship('Game', backref=db.backref('games',
                                                      order_by=review_id))

    def __repr__(self):
        """Provides helpful representation when printed"""

        return "<Review review_id={} game_id={} review={}>".format(
                self.review_id, self.game_id, self.review)


class User(db.Model):
    """User of Gaming website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """Provies helpful representation when printed"""

        return "<User user_id={} username={} password={} email={} register_date={}".format(
            self.user_id, self.username, self.password, self.email, 
                        self.register_date)


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
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # For convenience. if we run this module interactively,
    # it will leave you in a state of being able to work with 
    # the database directly.

    from server import app
    connect_to_db(app)
    print('Connected to GameOn-Line Database')