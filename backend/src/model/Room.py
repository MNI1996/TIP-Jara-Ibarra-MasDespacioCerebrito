from mongoengine import EmbeddedDocumentListField, IntField, Document
from backend.src.model.Round import Round


class Room(Document):

    id= IntField(primary_key=True)
    participants = IntField
    #round=EmbeddedDocumentListField(Round,default=[])
