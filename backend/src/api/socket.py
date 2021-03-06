from flask_socketio import Namespace, emit, join_room, leave_room
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

    def on_round_start(self, data):
        print(data, flush=True)
        room = data['room']
        emit('round_started', room=room)

    def on_end_round(self, data):
        room = data['room']
        print("terminando ronda de la room", flush=True)
        print(room, flush=True)
        emit('round_finished', room=room)

    def on_end_game(self, data):
        room = data['room']
        print("terminando la partida de la room", flush=True)
        print(room, flush=True)
        emit('game_ended', room=room)
        emit('get_game_state', {'room': room})

    def on_get_game_state(self, data):
        room = data['room']
        current_game_state = Room.objects.getPointsForAllPlayers(room)
        print("Actualizando el game state de" + room, flush=True)
        print(current_game_state, flush=True)
        emit('game_state_update', current_game_state)

    def on_update_room(self, data):
        room = data['room']
        print(f"Sala: {room} actualizada", flush=True)
        emit('room_updated', room=room)

    def on_leave_room(self, data):
        player = data['player']
        room = data['room']
        leave_room(room)
        a_player = Player.objects.get(nick=player)
        try:
            a_room = Room.objects.get(name=room)
            if player == a_room.owner.nick:
                print("OWNER:" + player + " left the room " + a_room.name, flush=True)
                print("The room is being deleted", flush=True)
                a_room.delete()
                emit("room_deleted", room=room)
            else:
                print(player + " left the room " + a_room.name, flush=True)
                Room.objects.remove_participant(room_name=a_room.name, a_participant=a_player)
            emit("player_left_room", room=room)
        except DoesNotExist:
            emit("leave_failed", room=room)

    def on_player_answered(self, data):
        print("ON PLAYER ANSWERED", flush=True)
        print(data, flush=True)
        room = data['room']
        question_id = data['question_id']
        a_room = Room.objects.get(name=room)
        a_room.reload()
        a_round = Room.objects.getRoundForAQuestion(room, question_id)
        print("cantidad de respuestas")
        print(len(a_round.answers), flush=True)
        print("cantidad de participantes")
        print(len(a_room.participants), flush=True)
        print("Actualizando el game state luego de una respuesta")
        current_game_state = Room.objects.getPointsForAllPlayers(room)
        print("Actualizando el game state de " + room, flush=True)
        print(current_game_state, flush=True)
        emit('game_state_update', current_game_state)
