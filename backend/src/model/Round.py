from mongoengine import ReferenceField, EmbeddedDocument, EmbeddedDocumentListField

from backend.src.model.Answer import Answer
from backend.src.model.Question import Question


class Round(EmbeddedDocument):
    question = ReferenceField(Question)
    answers = EmbeddedDocumentListField(Answer, default=[])

