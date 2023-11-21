from mongoengine import Document,StringField,IntField

class BookEntity(Document):
    
    title: str = StringField(required=True)
    author: str = StringField(required=True)
    description: str = StringField()
    year: int = IntField()
    