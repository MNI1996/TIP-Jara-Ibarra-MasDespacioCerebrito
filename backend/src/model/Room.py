from mongoengine import IntField, Document, ReferenceField, ListField, QuerySet, StringField

from backend.src.model.Player import Player


class Category(Document):
    name = StringField(primary_key=True)


# TODO: Rename to RoomManager and extract to another file
class RoomQuerySet(QuerySet):
    def add_participant(self, room_id, a_participant):
        print(id, a_participant, flush=True)
        a_room = Room.objects(id=room_id).first()
        if a_room.owner.nick != a_participant.nick:
            a_room.update(add_to_set__participants=a_participant)


class Room(Document):
    name = StringField(primary_key=True)
    owner = ReferenceField(Player)
    participants = ListField(ReferenceField(Player), default=[])
    rounds = IntField(default=5)
    categories = ListField(ReferenceField(Category), default=[])
    meta = {'queryset_class': RoomQuerySet}

    def __str__(self):
        return f"ID: {self.id}, participants: {self.participants}"
