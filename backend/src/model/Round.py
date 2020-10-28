from mongoengine import Document, ReferenceField, ListField

from backend.src.model.Answer import Answer
from backend.src.model.Question import Question
from backend.src.model.Room import Room


class Round(Document):
    room = ReferenceField(Room)
    question = ReferenceField(Question)
    answers = ListField(ReferenceField(Answer), default=[])

