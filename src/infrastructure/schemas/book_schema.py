from pydantic import BaseModel,Field
from typing import Optional
from bson.objectid import ObjectId as BsonObjectId

class BookPostRequest(BaseModel):
    
    title:str = Field("Harry Potter and the Philosopher's Stone")
    
    author:str = Field("J. K. Rowling")
    
    description:str = Field("Lorem ipsum dolor sit amet")
    
    year:int = Field(1997)
    
class BookSchema(BookPostRequest):
    
    id:Optional[BsonObjectId] = Field(default=None,alias="_id")
    
    class Config:
        
        populate_by_field_name = True #permite que se usen campos alternativos al crear instancias de la clase
        arbitrary_types_allowed = True #permite que se usen campos alternativos al crear instancias de la clase
        json_encoders = { #asegurar que los ObjectId se serialicen correctamente a texto cuando se convierten a JSON.
            BsonObjectId: lambda v: str(v)
        }