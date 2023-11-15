from src.domain.models.book_entity import BookEntity as Book
from src.infrastructure.repositories.interfaces.book_interface import BookInterface
from src.infrastructure.configs.database import db_connect

class BookRepository(BookInterface):
    
    def __init__(self) -> None:
        
        self.db = db_connect()
    
    def create(self, book: Book) -> Book:
        
        book.save()
        
        return book