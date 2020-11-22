# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource, abort

from mongoengine import DoesNotExist, ValidationError
# mongo-engine models
from backend.src.model.Player import Player


class LoginApi(Resource):

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        password = data.get('password', None)
        if not password or password == "":
            abort(400, message="No envió una password")
        try:
            post_player = Player.objects.get(nick=data['nick'])
            if post_player.password == password:
                return jsonify({'result': post_player})
            else:
                abort(400, message="Contraseña incorrecta")
        except DoesNotExist:
            abort(400, message="Usuario incorrecto")


class RegisterApi(Resource):

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        password = data.get('password', None)
        if not password or password == "":
            abort(400, message="No envió una password")
        try:
            post_player = Player.objects.get(nick=data['nick'])
            abort(400, message="Ese usuario ya existe")
        except DoesNotExist:
            post_player = Player(**data)
            try:
                post_player.save()
                return jsonify({'result': post_player})
            except ValidationError as e:
                abort(400, message=e.message)
