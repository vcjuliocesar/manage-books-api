from src.domain.models.book_entity import BookEntity as Book
from src.infrastructure.repositories.interfaces.book_interface import BookInterface

class BookRepository(BookInterface):
    
    def __init__(self) -> None:
        
        self.collection = "books"
    
    def create(self, book: Book) -> Book:
        
        return book