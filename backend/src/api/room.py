# flask packages
from flask import jsonify
from flask_restful import Resource, abort

# mongo-engine models
from mongoengine import DoesNotExist

from backend.src.model.Room import Room


class RoomsApi(Resource):
    def get(self):
        output = Room.objects()
        return jsonify({'result': output})


class RoomApi(Resource):
    def get(self, room_id):
        try:
            output = Room.objects.get(id=room_id)
        except DoesNotExist:
            raise abort(404)
        return jsonify({'result': output})
