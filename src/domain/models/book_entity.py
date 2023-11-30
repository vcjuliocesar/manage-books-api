from typing import Optional
from mongoengine import Document, StringField, IntField, ObjectIdField


class BookEntity(Document):
    #_id: Optional[str] = ObjectIdField()
    title: str = StringField(required=True)
    author: str = StringField(required=True)
    description: str = StringField()
    year: int = IntField()
