from flask import Flask

from app.config.config_dev import ConfigDev

def criar_app():
    app = Flask(__name__)

    app.config.from_object(ConfigDev)

    return app

