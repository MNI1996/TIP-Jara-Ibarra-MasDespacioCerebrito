from mongoengine import StringField, EmbeddedDocument


class Answer(EmbeddedDocument):
    player_id = StringField()
    question_option_id = StringField()
