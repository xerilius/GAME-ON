![Banner](static/img/gbanner.PNG)
<br/>
GAME-ON is a web app that allows users to discover, rate and review games. Users are able to register and log into their account, modify ratings and delete their game reviews. All data on games are from IGDB's API.

## Contents
* [Tech Stack](#technologies)
* [Features](#features)
* [Installation](#install)
* [Version 2.0](#version)
* [About Me](#aboutme)

## <a name="technologies"></a>🎮Technologies
**Backend:** 🐍 Python , Flask, PostgreSQL, SQLAlchemy <br/>
**Frontend:** JavaScript, AJAX, jQUERY, Jinja2, Boostrap, HTML5, CSS3 <br/>
**APIs:** IGDB <br/>

## <a name="features"></a>🎮Features
Discover: popular, recommended, anticipated and trending games. <br/>
Create an account and login <br/>
Search for games <br/>
Rate games <br/>
Review games <br/>

## <a name="install"></a>🎮Installation
##### To run GAME-ON: <br/>
**Clone or fork this repo**:
```
$ git clone https://github.com/xerilius/GAME-ON.git
```
**Create and  activate a virtual environment inside the GAME-ON directory:**
```
$ virtualenv env
$ source env/bin/activate
```
**Install the dependencies:**
```
$ pip install -r requirements.txt
```
**Sign-up to use [IGDB's API](https://api.igdb.com/signup). <br/>
Save your API key :key: in a file <kbd>secrets.sh</kbd> with this format:**
```
export SECRET_KEY = "PUT_YOUR_KEY_HERE"
export IGDB_API_KEY = "PUT_YOUR_KEY_HERE"
```
**Source your keys from <kbd>secrets.sh</kbd>:**
```
$ source secrets.sh
```
**Set up the database:**
```
$ createdb gameon
```
**Seed data into database:**
```
$ python3 seed.py
```
**Run the app:**
```
$ python3 server.py
```
**In your web browser, type in `localhost:5000` in the URL bar to access GAME-ON.**

## <a name="version"></a>🎮Version 2.0
* Edit reviews
* Allow users to add favorite games
* Newsfeed for games
* Videos of games on game details page
* More info of games


## <a name="aboutme"></a>🎮About Me
Grace Chung is an avid gamer and a software engineer. <br/>
To learn more about me, check out my [LinkedIn](http://www.linkedin.com/in/chung-grace)!
