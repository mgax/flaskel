import flask


views = flask.Blueprint('views', __name__,
                        static_folder='static',
                        template_folder='templates')


@views.route('/')
def home():
    return flask.render_template('home.html')
