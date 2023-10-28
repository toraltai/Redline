from flask import Flask
from extension.utils import *
from decouple import config

from datetime import timedelta


class BaseConfig:
    SECRET_KEY = 'askldnasjkldnasjkdnbasjvcx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    PERMANENT_SESSION_LIFETIME =  timedelta(minutes=10)


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    db.init_app(app)
    ip_ban.init_app(app)
    return app