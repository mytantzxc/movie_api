from datetime import datetime

from flask import request
from flask_restx import fields, Namespace, Resource
from models.movie import Movie
from models.genre import Genre

movie_namespace = Namespace('movies', description="Bebra movies")

movie_model = movie_namespace.model(
    'Movie',
    {
        'title': fields.String,
        'year': fields.Integer,
        'rate': fields.Integer,
        'genres': fields.List(fields.String)
    },
)


@movie_namespace.route("")
class GetMovies(Resource):

    @staticmethod
    def get():
        return {
                   'Movies': [
                       {
                           'title': movie.title,
                           'year': movie.year,
                           'rate': movie.rate,
                           'uploaded': str(movie.uploaded),
                           'genres': [
                               {'genre_name': genre.name} for genre in movie.genres
                           ]
                       } for movie in Movie.get_all()
                   ]
               }, 200


@movie_namespace.route("/post")
class PostMovie(Resource):

    @staticmethod
    @movie_namespace.expect(movie_model)
    def post():
        args = request.json
        title = args.get('title'),
        year = args.get('year'),
        rate = args.get('rate'),
        uploaded = datetime.utcnow()
        if Movie.exists(title):
            return {"Error": "Movie already exists"}, 409
        movie = Movie(
            title=title,
            year=year,
            rate=rate,
            uploaded=uploaded
        )
        movie.save()
        genres = args.get('genres')
        for genre_name in genres:
            genre = Genre.exists(genre_name)
            if not genre:
                genre = Genre(genre_name)
                genre.save()
            movie.add_genre(genre)
        return {'Notification': 'Movie saved'}, 201


