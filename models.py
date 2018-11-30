from flask_sqlalchemy import SQLAlchemy
from backend import shorten

db = SQLAlchemy()


class Url(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    short_url = db.Column(db.String(16), unique=True, nullable=False)

    url = db.Column(db.String(2000), unique=True, nullable=False, index=True)

    @staticmethod
    def add_url(url):
        new_url = Url(short_url='', url=url)
        db.session.add(new_url)
        db.session.flush()
        new_url.short_url = shorten(new_url.id)
        db.session.commit()
        return new_url

    @staticmethod
    def get_all_urls():
        return Url.query.all()

    def __str__(self):
        return 'Url %r - %r - %r' % (self.id, self.short_url, self.url)

    def __repr__(self):
        return '<Url %r - %r - %r>' % (self.id, self.short_url, self.url)
