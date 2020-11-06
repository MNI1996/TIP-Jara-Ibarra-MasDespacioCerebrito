from bson import ObjectId
from mongoengine import StringField, EmbeddedDocument, ObjectIdField


class Answer(EmbeddedDocument):
    id = ObjectIdField(required=True, default=lambda: ObjectId(), primary_key=True)
    player_id = StringField()
    question_option_id = StringField()
