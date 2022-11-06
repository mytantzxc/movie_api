from . import db
from sqlalchemy.dialects.postgresql import INTEGER

movie_genre = db.Table(
    'movie_genre',
    db.Column('movie_id', INTEGER, db.ForeignKey('movie.id'), primary_key=True, nullable=False),
    db.Column('genre_id', INTEGER, db.ForeignKey('genre.id'), primary_key=True, nullable=False)
)
