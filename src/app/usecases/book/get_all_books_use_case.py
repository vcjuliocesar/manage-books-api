from bson import ObjectId
from fastapi import Depends
from src.infrastructure.schemas.book_schema import BookPostRequest
from src.domain.services.book_service import BookService
from src.domain.models.book_entity import BookEntity

class GetAllBooksUseCase:
    
    def __init__(self,book_service:BookService = Depends()) -> None:
        
        self.book_service = book_service
        
    def execute(self) -> BookEntity:
        
        try:
            
            return self.book_service.get_all()
        
        except Exception as error:
            
            raise error