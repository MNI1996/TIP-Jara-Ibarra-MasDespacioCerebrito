from mongoengine import Document, StringField, EmbeddedDocumentListField

from backend.src.model.QuestionOption import QuestionOption


class Question(Document):
    text = StringField(required=True)
    options = EmbeddedDocumentListField(QuestionOption, default=[])
