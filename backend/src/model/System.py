from backend.src.model.Room import Room


class System:
    def __init__(self):
        self.rooms = []
        self.users = []

    def generateRoom(self, participants=2):
        self.rooms.append(Room(participants))
