from mongoengine import Document, StringField, EmbeddedDocumentListField, ListField, ReferenceField

from backend.src.model.Category import Category
from backend.src.model.QuestionOption import QuestionOption


class Question(Document):
    text = StringField(required=True)
    options = EmbeddedDocumentListField(QuestionOption, default=[])
    categories = ListField(ReferenceField(Category), default=[])
