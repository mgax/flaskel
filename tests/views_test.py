import flask
import unittest


class HomepageTest(unittest.TestCase):

    def setUp(self):
        self.app = flask.Flask(__name__)
        self.app.testing = True

    def test_homepage_returns_404(self):
        client = self.app.test_client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 404)
