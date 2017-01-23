from flask import Flask


def configure_routes(app):
    from .routes import home_page, sendmessage
    app.add_url_rule('/', view_func=home_page)
    app.add_url_rule('/SendMessage/', view_func=sendmessage, methods=['POST'])

def create_app(**config):
    app = Flask(__name__)
    app.config['DEBUG'] = True
    configure_routes(app)
    return app
