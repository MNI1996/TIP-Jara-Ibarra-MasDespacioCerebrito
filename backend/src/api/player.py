# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource

# mongo-engine models
from backend.src.model.Player import Player


class PlayerApi(Resource):
    @staticmethod
    def get() -> Response:
        output = Player.objects().first()
        return jsonify({'result': output})

    @staticmethod
    def post() -> Response:
        data = request.get_json()
        post_player = Player(**data)
        post_player.save()
        return jsonify({'result': post_player})
