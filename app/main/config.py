import os
from decouple import config

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = config('DB_CONNECTION')
    DEBUG = True
