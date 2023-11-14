from src.infrastructure.repositories.book_repository import BookRepository
from src.infrastructure.schemas.book_schema import BookSchema
from src.domain.models.book_entity import BookEntity as Book

class BookService:
    
    def __init__(self) -> None:
        
        self.repository = BookRepository()
        
    def create(self,book:BookSchema) -> Book:
        print("Holaaaaaaaaaaaaaaa")
        return self.repository.create(Book(**book.model_dump()))