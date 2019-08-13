"""Models and database functions"""
from flask_sqlalchemy import SQLAlchemy


# This is the connection to the PostgreSQL database via Flask-SQLAlchemy to use session

db = SQLAlchemy()

# Model defintions

class Game(db.Model):
    """Games on gaming website."""

    __tablename__ = "games"

    game_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False)
    # developer = db.Column(db.String, nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Game game_id={} title={} genre={} img_url={} description={} release_date={}>"
                .format(self.game_id, self.title, self.genre, self.img_url,
                        self.description, self.release_date)




class Rating(db.Model):
    """Rating of game by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.games_id'), nullable=False)
    star_rating = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

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
    user = db.realtionship('User', backref=db.backref('reviews',
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

        return "<User user_id={} username={} password={} email={} register_date={}"
                .format(self.user_id, self.username, self.password, self.email, 
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
