import flask


def create_app():
    app = flask.Flask(__name__)
    return app


if __name__ == '__main__':
    create_app().run()
