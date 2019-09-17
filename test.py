from server import app
import unittest
import server
from unittest import TestCase
from flask  import flask

class FlaskTests(unittest.TestCase):
    """Test for GAME-ON"""

    def setUp(self):
        self.cliet = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        resut = self.client.get('/')
        self.assertTrue('homepage.html')

    def test_login(self):
        result = self.client.post("/login",
                                    data= {"user_id": 1,
                                            "password": "abc"},
                                            follow_redirects=True)
        self.assertIn("Welcome back", result.data)
