from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema
from implemented import genre_service
from service.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


@genre_ns.route('')
class  GenresView(Resource):
    @auth_required
    def get(self):
        genre = genre_service.get_all()
        return genres_schema.dump(genre)

    @admin_required
    def post(self):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404
        genre = genre_service.create(req_json)
        return genre_schema.dump(genre), 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        genre = genre_service.get_one(gid)
        if not genre:
            return "такого жанра нет", 404
        return genre_schema.dump(genre), 201

    @admin_required
    def put(self, gid):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = gid

        genre = genre_service.update(req_json)
        return genre_schema.dump(genre), 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204