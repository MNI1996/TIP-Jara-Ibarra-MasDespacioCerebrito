from mongoengine import Document, StringField, BooleanField


class QuestionOption(Document):
    sentence = StringField(required=True)
    correct = BooleanField(required=True)
