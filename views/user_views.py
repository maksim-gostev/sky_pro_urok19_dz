from flask_restx import Resource, Namespace
from flask import request

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')

users_schema = UserSchema(many=True)
user_schema = UserSchema()

@user_ns.route('')
class UsersView(Resource):
    def get(self):
      users = user_service.get_all()
      return users_schema.dump(users), 200

    def post(self):
        req_json = request.json

        if not req_json:
            return "вы не ввели данные", 404

        user = user_service.create(req_json)
        return user_schema.dump(user), 201

@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return user_schema.dump(user), 200

    def put(self, uid):
        req_json = request.json
        if not req_json:
            return "вы не ввели данные", 404

        req_json['id'] = uid

        user = user_service.update(req_json)
        return user_schema.dump(user), 204