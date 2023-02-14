from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from service.decorators import auth_required, admin_required

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('')
class MoviesView(Resource):
    @auth_required
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
        }
        all_movies = movie_service.get_all(filters)

        return movies_schema.dump(all_movies), 200

    @admin_required
    def post(self):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one(mid)
        if not movie:
            return "такого фильма нет", 404
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, mid):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = mid

        movie = movie_service.update(req_json)
        return movie_schema.dump(movie), 204

    @admin_required
    def delete(self, mid):
        movie_service.delete(mid)
        return "", 204
