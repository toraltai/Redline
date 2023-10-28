from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()


class BaseConfig:
    SECRET_KEY = 'askldnasjkldnasjkdnbasjvcx'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')
    db.init_app(app)
    return app