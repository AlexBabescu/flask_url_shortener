from flask import Flask
from models import db

import views


application = Flask(__name__)

application.config.from_pyfile('config.py')

application.register_blueprint(views.blueprint)


@application.before_first_request
def create_tables():
    db.create_all()
    db.session.commit()


db.init_app(application)
