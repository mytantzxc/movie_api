from . import db
from sqlalchemy.dialects.postgresql import INTEGER


class MovieGenre(db.Model):
    db.Table.name = 'movie_genre'

    movie_id = db.Column(
        INTEGER, db.ForeignKey('movie.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False
    )
    genre_id = db.Column(
        INTEGER, db.ForeignKey('genre.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False
    )

    def __init__(self, movie_id, genre_id):
        self.movie_id = movie_id
        self.genre_id = genre_id
