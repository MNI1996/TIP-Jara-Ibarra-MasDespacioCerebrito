from mongoengine import Document, StringField


class Category(Document):
    name = StringField(primary_key=True)
