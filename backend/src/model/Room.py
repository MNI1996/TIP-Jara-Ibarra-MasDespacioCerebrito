from mongoengine import IntField, Document, ReferenceField, ListField, QuerySet

from backend.src.model.Player import Player


class RoomQuerySet(QuerySet):
    def add_participant(self, room_id, a_participant):
        print(id, a_participant, flush=True)
        Room.objects(id=room_id).update(add_to_set__participants=a_participant)


class Room(Document):
    id = IntField(primary_key=True)
    owner = ReferenceField(Player)
    participants = ListField(ReferenceField(Player), default=[])
    meta = {'queryset_class': RoomQuerySet}

    def __str__(self):
        return f"ID: {self.id}, participants: {self.participants}"
