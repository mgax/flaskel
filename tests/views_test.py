import flask
import unittest


class HomepageTest(unittest.TestCase):

    def setUp(self):
        from views import views
        self.app = flask.Flask(__name__)
        self.app.testing = True
        self.app.register_blueprint(views)

    def test_homepage_returns_hello_text(self):
        client = self.app.test_client()
        resp = client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, "Hello Flask!")
