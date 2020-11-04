from mongoengine import Document, StringField


class Answer(Document):
    player_id = StringField()
    question_option_id = StringField()