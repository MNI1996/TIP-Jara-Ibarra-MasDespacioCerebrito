from mongoengine import EmbeddedDocumentListField, IntField, Document
from backend.src.model.Round import Round


class Room(Document):
    id = IntField(primary_key=True)
    participants = IntField(default=1)
    #round=EmbeddedDocumentListField(Round,default=[])

    def __str__(self):
        return f"ID: {self.id}, participants: {self.participants}"
