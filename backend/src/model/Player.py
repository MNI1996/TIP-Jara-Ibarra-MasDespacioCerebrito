from mongoengine import StringField, Document


class Player(Document):

    nick = StringField(required=True, primary_key=True)
