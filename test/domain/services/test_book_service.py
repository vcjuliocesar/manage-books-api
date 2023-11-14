import datetime
from bson import ObjectId
import pytest
from src.domain.services.book_service import BookService
from src.domain.models.book_entity import BookEntity
from src.infrastructure.schemas.book_schema import BookSchema

def test_it_can_create_book():
    
    book_service = BookService()
    
    book_schema = BookSchema(
        title = "Harry Potter and the Philosopher's Stone",
        author = "J. K. Rowling",
        description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        year = 1997 
    )
    
    book_entity = book_service.create(book_schema)
    
    assert isinstance(book_entity,BookEntity)
    
    assert book_entity.title == "Harry Potter and the Philosopher's Stone"
    
    assert book_entity.author == "J. K. Rowling"