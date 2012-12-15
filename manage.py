#!/usr/bin/env python

import os
import flask
from flask.ext.script import Manager


DEBUG = (os.environ.get('DEBUG') == 'on')


def create_app():
    from views import views

    app = flask.Flask(__name__)
    app.debug = DEBUG
    app.register_blueprint(views)

    @app.route('/_crashme')
    def crashme():
        raise RuntimeError("Crashing, as requested.")

    return app


manager = Manager(create_app)


if __name__ == '__main__':
    manager._commands['runserver'].use_reloader = DEBUG
    manager.run()
