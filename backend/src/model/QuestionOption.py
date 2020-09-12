from bson import ObjectId
from mongoengine import StringField, BooleanField, EmbeddedDocument, ObjectIdField


class QuestionOption(EmbeddedDocument):
    _id = ObjectIdField(required=True, default=lambda: ObjectId())
    sentence = StringField(required=True)
    correct = BooleanField(required=True, default=False)
