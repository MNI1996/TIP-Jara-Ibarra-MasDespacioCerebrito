from flask_socketio import Namespace, emit, send, join_room
from mongoengine import DoesNotExist

from backend.src.model.Player import Player
from backend.src.model.Room import Room


class RoomSocket(Namespace):

    def on_connect(self):
        print("me conecté wachin", flush=True)

    def on_disconnect(self):
        pass

    def on_my_event(self, data):
        print("evento personalizado", flush=True)
        emit('my_response', data)

    def on_join(self, data):
        print("joined", flush=True)
        print(data, flush=True)
        username = data['username']
        room = data['room']
        join_room(room)
        send(username + ' has entered the room.', room=room)
        a_player = Player.objects.get(nick=username)
        try:
            a_room = Room.objects.get(id=room)
            Room.objects.add_participant(room_id=a_room.id, a_participant=a_player)
        except DoesNotExist:
            a_room = Room(id=room)
            a_room.owner = a_player
            a_room.save()
        print(a_room, flush=True)

    def on_start(self, data):
        room = data['room']
        send('Game Started', room=room)

