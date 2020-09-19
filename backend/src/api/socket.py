from flask_socketio import Namespace, emit


class RoomSocket(Namespace):

    def on_connect(self):
        print("me conecté wachin", flush=True)

    def on_disconnect(self):
        pass

    def on_my_event(self, data):
        print("evento personalizado", flush=True)
        emit('my_response', data)
