#!/usr/bin/env python

import flask
from flask.ext.script import Manager


def create_app():
    from views import views
    app = flask.Flask(__name__)
    app.register_blueprint(views)
    return app


manager = Manager(create_app)


if __name__ == '__main__':
    manager.run()
