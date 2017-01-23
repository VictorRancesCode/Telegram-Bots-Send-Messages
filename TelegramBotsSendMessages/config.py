import configparser

from flask import Flask


def create_app(**config):
    app = Flask(__name__)
    app.config['DEBUG'] = True

    config = configparser.ConfigParser()
    config.sections()
    config.read('settings.ini')

    app.config['TELEGRAM'] = config['Telegram']
    return app
