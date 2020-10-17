from flask_socketio import Namespace, emit, send, join_room
from mongoengine import DoesNotExist

from backend.src.model.Player import Player
from backend.src.model.Room import Room


class RoomSocket(Namespace):

    def on_connect(self):
        print("me conecté wachin", flush=True)

    def on_disconnect(self):
        print("se salió", flush=True)

    def on_my_event(self, data):
        print("evento personalizado", flush=True)
        emit('my_response', data)

    def on_join(self, data):
        username = data['username']
        room = data['room']
        join_room(room)
        a_player = Player.objects.get(nick=username)
        try:
            a_room = Room.objects.get(name=room)
            Room.objects.add_participant(room_name=a_room.name, a_participant=a_player)
            emit("joined_room", room=room)
        except DoesNotExist:
            emit("join_failed", room=room)

    def on_start(self, data):
        room = data['room']
        emit('game_started', room=room)

