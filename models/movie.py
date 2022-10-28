from . import db
from sqlalchemy.dialects.postgresql import VARCHAR, INTEGER


class Movie(db.Model):
    db.Table.name = 'Movie'

    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(255), nullable=False)
    genre = db.Column(VARCHAR(255), nullable=False)

    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __repr__(self):
        return f"Movie {self.title},{self.genre}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls) -> tuple:
        return db.session.query(Movie)


