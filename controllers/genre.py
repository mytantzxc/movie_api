from flask_restx import fields, Namespace, Resource
from models.genre import Genre

genre_namespace = Namespace('genres', description='Bebra genres')

genre_model = genre_namespace.model(
    'Genre',
    {
        'genre_name': fields.String
    }
)


@genre_namespace.route("")
class GetGenre(Resource):
    @staticmethod
    def get() -> tuple:
        genre_list = Genre.get_all()

        if genre_list:
            genres_json = [
                {
                    'genre_id': genre.id,
                    'genre_name': genre.name
                }
                for genre in genre_list
            ]
            return {'genres': genres_json}, 200
        return {'Error': 'Not found'}, 404
