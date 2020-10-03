# flask packages
from flask import jsonify
from flask_restful import Resource

# mongo-engine models
from backend.src.model.Room import Room


class RoomApi(Resource):
    def get(self):
        output = Room.objects()
        return jsonify({'result': output})
