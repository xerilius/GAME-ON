from jinja2 import StrictUndefined
import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, Game

app = Flask(__name__)

# # Required to use Flask session and debug toolbar.
# # to create Flask.secret_key(or SECRET_KEY) do:
#     # $ python -c 'import os; print(os.urandom(16))'
#     # >>> import os
#     # >>> os.urandom(24)
    
# # set a 'SECRET_KEY' to enable the Flask session cookies
# # app.config['SECRET_KEY'] = '<replace with a secret key>'
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
# This raises an error for silent error caused by undefined variable in Jinja2
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """Homepage"""

    return render_template("homepage.html")


if __name__ == "__main__":

    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")