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
        players = Player.objects()
        return jsonify({'result': output, 'players': players})

    @staticmethod
    def post() -> Response:
        owner_name = request.json['owner']
        room_name = request.json['name']
        categories = request.json.get('categories', [])
        rounds_amount = request.json.get('rounds_amount', 4)
        round_time = request.json.get('round_time', 10)
        try:
            player = Player.objects.get(nick=owner_name)
        except DoesNotExist:
            raise abort(404)
        post_room = Room(name=room_name, owner=player, rounds_amount=rounds_amount, round_time=round_time)
        try:
            post_room.save()
        except ValidationError as e:
            raise abort(400, message=e.message)
        for c in categories:
            try:
                category = Category(name=c)
                post_room.update(add_to_set__categories=category)
                post_room.reload()
            except DoesNotExist:
                raise abort(404)
        rounds = Room.objects.getRoundsFor(post_room.name)
        for round_obj in rounds:
            post_room.update(add_to_set__rounds=round_obj)
            post_room.reload()
        return jsonify({'result': post_room})


class RoomApi(Resource):
    def get(self, room_id):
        try:
            output = Room.objects.get(name=room_id)
            players = Player.objects(nick__in=[p.id for p in output.participants])
        except DoesNotExist:
            raise abort(404)
        return jsonify({'result': output, 'players': players})


class RoomsUpdateApi(Resource):

    @staticmethod
    def post(room_id) -> Response:
        room_name = room_id
        try:
            room = Room.objects.get(name=room_name)
        except DoesNotExist:
            raise abort(404, message="La Sala no Existe")

        categories = request.json.get('categories', [c.id for c in room.categories])
        rounds_amount = request.json.get('rounds_amount', room.rounds_amount)
        round_time = request.json.get('round_time', room.round_time)

        try:
            Room.objects(name=room_name).update(categories=[], rounds_amount=rounds_amount, round_time=round_time, rounds=[])
            for c in categories:
                try:
                    category = Category(name=c)
                    room.update(add_to_set__categories=category)
                    room.reload()
                except DoesNotExist:
                    raise abort(404, message="Categoria incorrecta")
            room.reload()
        except ValidationError as e:
            raise abort(400, message=e.message)
        rounds = Room.objects.getRoundsFor(room_name)
        for round_obj in rounds:
            room.update(add_to_set__rounds=round_obj)
            room.reload()
        return jsonify({'result': room})
