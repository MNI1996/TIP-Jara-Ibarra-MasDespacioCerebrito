# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource, abort

from mongoengine import DoesNotExist
# mongo-engine models
from backend.src.model.Player import Player


class PlayerApi(Resource):
    @staticmethod
    def get() -> Response:
        data_nick = request.args['nick']
        try:
            output = Player.objects.get(nick=data_nick)
        except DoesNotExist:
            raise abort(404)
        return jsonify({'result': output})

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        try:
            post_player = Player.objects.get(nick=data['nick'])
        except DoesNotExist:
            post_player = Player(**data)
            post_player.save()
        return jsonify({'result': post_player})
