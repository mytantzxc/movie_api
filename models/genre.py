from . import db
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR


class Genre(db.Model):
    db.Table.name = 'genre'
    id = db.Column(INTEGER, primary_key=True)
    name = db.Column(VARCHAR(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Genre {self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def exists(cls, genre_name):
        return Genre.query.filter(Genre.name == genre_name).first()
