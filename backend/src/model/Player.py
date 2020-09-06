from backend.src.model import System


class Player:

    def __init__(self, name):
        self.nick = name

    def joinToRoom(self, roomId):
        System.rooms.get[roomId].add(self)

    def answer(self, round):
        input=input()
        return round.resolve(input)
