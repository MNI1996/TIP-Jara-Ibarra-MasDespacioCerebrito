# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource, abort

# mongo-engine models
from mongoengine import DoesNotExist, ValidationError

from backend.src.model.Player import Player
from backend.src.model.Room import Room, Category


class RoomsApi(Resource):
    def get(self):
        output = Room.objects()
        return jsonify({'result': output})

    @staticmethod
    def post() -> Response:
        owner_name = request.json['owner']
        room_name = request.json['name']
        categories = request.json.get('categories', [])
        try:
            player = Player.objects.get(nick=owner_name)
        except DoesNotExist:
            raise abort(404)
        post_room = Room(name=room_name, owner=player)
        try:
            post_room.save()
        except ValidationError as e:
            raise abort(400, message=e.message)
        for c in categories:
            try:
                category = Category.objects.fields().filter(name=c).first()
                post_room.update(add_to_set__categories=category)
                post_room.reload()
            except DoesNotExist:
                raise abort(404)
        return jsonify({'result': post_room})


class RoomApi(Resource):
    def get(self, room_id):
        try:
            output = Room.objects.get(name=room_id)
        except DoesNotExist:
            raise abort(404)
        return jsonify({'result': output})
