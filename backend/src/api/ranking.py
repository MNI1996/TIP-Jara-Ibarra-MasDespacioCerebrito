# flask packages
from flask import jsonify, Response
from flask_restful import Resource
# mongo-engine models
from backend.src.model.Player import Player


class RankingApi(Resource):
    @staticmethod
    def get() -> Response:
        output = Player.objects.all().order_by('-points',)
        return jsonify({'result': output})
