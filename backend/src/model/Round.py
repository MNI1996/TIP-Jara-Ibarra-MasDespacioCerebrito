from bson import ObjectId
from mongoengine import ReferenceField, EmbeddedDocument, EmbeddedDocumentListField, ObjectIdField

from backend.src.model.Answer import Answer
from backend.src.model.Question import Question


class Round(EmbeddedDocument):
    id = ObjectIdField(required=True, default=lambda: ObjectId(), primary_key=True)
    question = ReferenceField(Question)
    answers = EmbeddedDocumentListField(Answer, default=[])

