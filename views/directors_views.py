from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from implemented import director_service
from service.decorators import auth_required, admin_required

director_ns = Namespace('directors')

directors_schema = DirectorSchema(many=True)
director_schema = DirectorSchema()

@director_ns.route('/')
class DirectorsView(Resource):
    # @auth_required
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200

    # @admin_required
    def post(self):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404
        director = director_service.create(req_json)
        return director_schema.dump(director), 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, did):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = did

        director = director_service.update(req_json)
        return director_schema.dump(director), 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
