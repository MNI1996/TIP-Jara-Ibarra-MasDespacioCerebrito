from flask_socketio import Namespace, emit, send, join_room


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
