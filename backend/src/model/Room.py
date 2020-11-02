from mongoengine import Document, ReferenceField, ListField, QuerySet, StringField, EmbeddedDocumentListField, IntField

from backend.src.model.Category import Category
from backend.src.model.Player import Player
from backend.src.model.Question import Question
from backend.src.model.Round import Round


class RoomManager(QuerySet):
    def add_participant(self, room_name, a_participant):
        a_room = Room.objects(name=room_name).first()
        if a_room.owner.nick != a_participant.nick:
            a_room.update(add_to_set__participants=a_participant)

    def remove_participant(self, room_name, a_participant):
        a_room = Room.objects(name=room_name).first()
        a_room.update(pull__participants=a_participant)

    def getRoundsFor(self, name):
        a_room = self.get(name=name)
        categories = a_room.categories
        round_amount = a_room.rounds_amount
        questions = Question.objects.filter(categories__in=categories)[:round_amount]

        rounds = []
        for question in questions:
            round = Round(question=question)
            rounds.append(round)
        return rounds


class Room(Document):
    name = StringField(primary_key=True)
    owner = ReferenceField(Player)
    participants = ListField(ReferenceField(Player), default=[])
    rounds_amount = IntField(default=5)
    rounds = EmbeddedDocumentListField(Round, default=[])
    categories = ListField(ReferenceField(Category), default=[])
    meta = {'queryset_class': RoomManager}

    def __str__(self):
        return f"ID: {self.id}, participants: {self.participants}"
