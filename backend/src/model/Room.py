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
        if not questions:
            questions = Question.objects.all()[:round_amount]
        rounds = []
        for question in questions:
            round = Round(question=question)
            rounds.append(round)
        return rounds

    def getPointsFor(self, room_name, player_nick):
        answers = self.getAllAnswersOf(room_name, player_nick)
        points_rate = 1
        currentPoints = len(answers) * points_rate
        return currentPoints

    def getAllAnswersOf(self, room_name, player_nick):
        a_room = self.get(name=room_name)
        answers = []
        for a_round in a_room.rounds:
            for answer in a_round.answers:
                if answer.player_id == player_nick and self.isAnswerCorrect(a_round.question, answer.question_option_id):
                    answers.append(answer)
        return answers

    def isAnswerCorrect(self, question, question_option_id):
        question_option = question.options.get(_id=question_option_id)
        return question_option.correct

    def getRoundForAQuestion(self, room_name, question_id):
        a_room = self.get(name=room_name)
        for round_obj in a_room.rounds:
            if str(round_obj.question.id) == question_id:
                return round_obj
        return None


class Room(Document):
    name = StringField(primary_key=True)
    owner = ReferenceField(Player)
    participants = ListField(ReferenceField(Player), default=[])
    rounds_amount = IntField(default=4)
    rounds = EmbeddedDocumentListField(Round, default=[])
    categories = ListField(ReferenceField(Category), default=[])
    meta = {'queryset_class': RoomManager}

    def __str__(self):
        return f"ID: {self.id}, participants: {self.participants}"
