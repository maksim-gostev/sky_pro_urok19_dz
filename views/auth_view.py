from flask import request
from flask_restx import Resource, Namespace
from service.auth_ser import authorization, authorization_put


auth_ns = Namespace('auth')

@auth_ns.route('')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        res = authorization(req_json)
        return res


    def put(self):
        req_json = request.json
        res = authorization_put(req_json)
        return res