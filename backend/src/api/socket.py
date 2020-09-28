from flask_socketio import Namespace, emit, send, join_room

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
        a_room = Room.objects.get(id=room)
        if not a_room:
            a_room = Room(id=room)
            a_room.save()
        else:
            a_room.participants = a_room.participants + 1
            a_room.save()
        print(a_room, flush=True)

