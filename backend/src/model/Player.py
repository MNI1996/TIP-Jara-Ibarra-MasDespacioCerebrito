from mongoengine import StringField, Document, IntField


class Player(Document):
    nick = StringField(required=True, primary_key=True)
    points = IntField(default=0)
