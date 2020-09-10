from mongoengine import Document, StringField, ListField, EmbeddedDocumentField

from backend.src.model.QuestionOption import QuestionOption


class Question(Document):
    text = StringField(required=True)
    options = ListField(EmbeddedDocumentField(QuestionOption, default=[]))
