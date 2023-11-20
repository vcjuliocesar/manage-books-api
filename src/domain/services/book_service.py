from bson import ObjectId
from src.infrastructure.repositories.book_repository import BookRepository
from src.infrastructure.schemas.book_schema import BookSchema
from src.infrastructure.exceptions.book_already_exists_exception import BookAlreadyExistsException
from src.infrastructure.exceptions.book_not_found_exception import BookNotFoundException
from src.domain.models.book_entity import BookEntity as Book

class BookService:
    
    def __init__(self) -> None:
        
        self.repository = BookRepository()
        
    def create(self,book:BookSchema) -> Book:
        
        exists = self.repository.find_one({"title":book.title})
        
        if exists:
                
            raise BookAlreadyExistsException()
        
        return self.repository.create(Book(**book.model_dump()))
    
    def find_one(self,criteria:dict) -> Book:
        
        return self.repository.find_one(criteria)
    
    def find_by_id(self,id_book:ObjectId) -> Book:
        
        book = self.repository.find_by_id(id_book)
        
        if not book:
            
            raise BookNotFoundException()
        
        return book
    
    def update(self,new_book:BookSchema) -> Book:
        
        book = self.find_by_id(new_book.id)
        
        if not book:
            
            raise BookNotFoundException()
        
        book.title = new_book.title
        
        book.author = new_book.author
        
        book.description = new_book.description
        
        book.year = new_book.year
        
        return self.repository.update(book)
        
    def delete(self,book:Book) -> None:
        
        if not self.find_by_id(book.id):
            
            raise BookNotFoundException()
        
        return self.repository.delete(book)
    
    def get_all(self) -> list[Book]:
        
        return self.repository.get_all()