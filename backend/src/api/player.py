# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource, abort

from mongoengine import DoesNotExist, ValidationError
# mongo-engine models
from backend.src.model.Player import Player


class PlayerApi(Resource):
    @staticmethod
    def get() -> Response:
        data_nick = request.args['nick']
        try:
            output = Player.objects.get(nick=data_nick)
        except DoesNotExist:
            raise abort(404, message="El jugador con ese Nick no Existe")
        return jsonify({'result': output})

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        password = data.get('password', None)
        if not password or password == "":
            abort(400, message="No envió una password")
        try:
            post_player = Player.objects.get(nick=data['nick'])
        except DoesNotExist:
            post_player = Player(**data)
            try:
                post_player.save()
            except ValidationError as e:
                abort(400, message=e.message)
        return jsonify({'result': post_player})
