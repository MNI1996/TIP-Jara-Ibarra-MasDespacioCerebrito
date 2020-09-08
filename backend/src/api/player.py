# flask packages
from flask import jsonify
from flask_restful import Resource

# mongo-engine models
from backend.src.model.Player import Player


class PlayerApi(Resource):
    def get(self):
        output = Player.objects()
        return jsonify({'result': output})