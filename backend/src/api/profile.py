from flask import Response, request, jsonify
from flask_restful import Resource, abort
from mongoengine import DoesNotExist, ValidationError

from backend.src.model.Player import Player


class UpdateProfileApi(Resource):

    @staticmethod
    def post(player_id) -> Response:
        try:
            player = Player.objects.get(nick=player_id)
        except DoesNotExist:
            raise abort(404, message="El jugador no existe")
        avatar_image = request.json.get('avatar_image', player.avatar_image_name)

        try:
            player.update(avatar_image_name=avatar_image)
            player.save()
            player.reload()
        except ValidationError as e:
            raise abort(400, message=e.message)
        return jsonify({'result': player})
