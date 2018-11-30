import os

SECRET_KEY = 'Super secret key'

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///url_shortener.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False