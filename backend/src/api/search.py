# flask packages
from flask import jsonify, Response, request
from flask_restful import Resource
from mongoengine import Q

# mongo-engine models
from backend.src.model.Player import Player
from backend.src.model.Room import Room


class SearchApi(Resource):

    @staticmethod
    def get() -> Response:
        search_string = request.args.get('q', None)
        output = Room.objects.filter(
            Q(name__icontains=search_string) | Q(owner__in=Player.objects.filter(nick__icontains=search_string)))
        return jsonify({'result': output})
