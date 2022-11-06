from flask import Flask
from config import Config
from flask_restx import Api
from models import db
from flask_migrate import Migrate
from controllers.movie import movie_namespace
from controllers.genre import genre_namespace


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


def init_migrate(app):
    migrate = Migrate(app, db)
    db.init_app(app)
    migrate.init_app(app, db)
    return migrate


app = create_app()
migrate = init_migrate(app=app)
api = Api(app)

api.add_namespace(movie_namespace)
api.add_namespace(genre_namespace)

if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)
    with app.app_context():
        db.drop_all()


