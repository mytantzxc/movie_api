from datetime import datetime

from . import db
from .movie_genre import movie_genre
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER, SMALLINT, TIMESTAMP


class Movie(db.Model):
    db.Table.name = 'movie'

    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(255), nullable=False)
    year = db.Column(INTEGER, nullable=False)
    rate = db.Column(SMALLINT, nullable=False)
    uploaded = db.Column(TIMESTAMP, nullable=False, default=datetime.utcnow())
    genres = db.relationship('Genre', secondary=movie_genre, backref=db.backref('movies', lazy=True))

    def __init__(self, title, year, rate, uploaded):
        self.title = title,
        self.year = year
        self.rate = rate,
        self.uploaded = uploaded,

    def __repr__(self):
        return f"Movie {self.title} {self.year} {self.rate}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def add_genre(self, genre):
        self.genres.append(genre)
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls) -> tuple:
        return db.session.query(Movie)

    @classmethod
    def exists(cls, title):
        return Movie.query.filter(Movie.title == title).first()


