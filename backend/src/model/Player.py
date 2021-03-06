from mongoengine import StringField, Document, IntField


class Player(Document):
    nick = StringField(required=True, primary_key=True, min_length=3)
    points = IntField(default=0)
    password = StringField(min_length=6)
    avatar_image_name = StringField(default="man")
