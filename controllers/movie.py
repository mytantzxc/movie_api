from flask_restx import fields, Namespace, Resource
from models.movie import Movie
from flask import request

movie_namespace = Namespace('movies', description="Bebra movies")

movie_model = movie_namespace.model(
    'Movie',
    {
        'title': fields.String,
        'genre': fields.String
    },
)


@movie_namespace.route("")
class GetMovies(Resource):

    @staticmethod
    def get():
        return {'Movies': [{'title': movie.title, 'genre': movie.genre} for movie in Movie.get_all()]}, 200


@movie_namespace.route("/post")
class PostMovie(Resource):

    @staticmethod
    @movie_namespace.expect(movie_model)
    def post():
        args = request.json
        movie = Movie(
            args.get('title'),
            args.get('genre')
        )
        movie.save()
        return {'Notification': 'Movie saved'}, 201


