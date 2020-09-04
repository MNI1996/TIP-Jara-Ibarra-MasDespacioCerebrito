from mongoengine import Document, StringField


class Question(Document):
    name = StringField(required=True)
    # options = EmbeddedDocumentListField(QuestionOption, default=[])
