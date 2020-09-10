from mongoengine import StringField, BooleanField, EmbeddedDocument


class QuestionOption(EmbeddedDocument):
    sentence = StringField(required=True)
    correct = BooleanField(required=True, default=False)
