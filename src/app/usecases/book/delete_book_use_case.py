from bson import ObjectId
from fastapi import Depends
from src.infrastructure.schemas.book_schema import BookPostRequest
from src.domain.services.book_service import BookService
from src.domain.models.book_entity import BookEntity

class DeleteBookUseCase:
    
    def __init__(self,book_service:BookService = Depends()) -> None:
        
        self.book_service = book_service
        
    def execute(self,id_book:ObjectId) -> BookEntity:
        
        try:
            
            return self.book_service.delete(id_book)
        
        except Exception as error:
            
            raise error