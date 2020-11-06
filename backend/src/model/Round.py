from mongoengine import ReferenceField, ListField, EmbeddedDocument

from backend.src.model.Answer import Answer
from backend.src.model.Question import Question


class Round(EmbeddedDocument):
    question = ReferenceField(Question)
    answers = ListField(ReferenceField(Answer), default=[])

    def resolve(self, answer):
        return self.question.options[answer].valuate()
