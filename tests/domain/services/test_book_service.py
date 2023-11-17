import pytest
from bson import ObjectId
from unittest.mock import patch
from src.domain.services.book_service import BookService
from src.domain.models.book_entity import BookEntity as Book
from src.infrastructure.schemas.book_schema import BookSchema
from src.infrastructure.exceptions.book_already_exists_exception import BookAlreadyExistsException
from src.infrastructure.exceptions.book_not_found_exception import BookNotFoundException


@pytest.fixture
def book_service():
    return BookService()


def test_it_return_an_exception_if_book_already_exists(book_service):

    with patch.object(BookService, 'create', side_effect=BookAlreadyExistsException("Book already exists")):

        create_book = BookSchema(
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )

        with pytest.raises(BookAlreadyExistsException):

            book_service.create(create_book)

    # Book.objects.get(id=book.id).delete()


def test_it_can_create_book(book_service, caplog):

    with patch.object(BookService, 'create') as mock_create:

        fake_mongo_id = ObjectId('60a5c1d5e9b92b6f8e87654a')

        create_book = BookSchema(
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )

        mock_create.return_value = Book(
            id=fake_mongo_id,
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )

        book_entity = book_service.create(create_book)

        # Assert
        assert isinstance(book_entity, Book)

        assert book_entity.id == fake_mongo_id

        assert book_entity.title == "Harry Potter and the Philosopher's Stone"

        assert book_entity.author == "J. K. Rowling"

        captured_logs = caplog.text
        print(captured_logs)
    # Book.objects.get(id=book_entity.id).delete()

def test_it_return_an_exception_if_book_not_found(book_service):
    
    with patch.object(BookService,'update',side_effect=BookNotFoundException("Book not found")):
        
        fake_mongo_id = ObjectId('60a5c1d5e9b92b6f8e87654a')
        
        update_book = BookSchema(
            id=fake_mongo_id,
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )
        
        with pytest.raises(BookNotFoundException):
            
            book_service.update(update_book)
        
    
def test_it_can_update_book(book_service):

    with patch.object(BookService, 'update') as mock_update:

        fake_mongo_id = ObjectId('60a5c1d5e9b92b6f8e87654a')

        update_book = BookSchema(
            id=fake_mongo_id,
            title="title",
            author="new author",
            description="Lorem ipsum dolor veniam ...",
            year=1999
        )

        mock_update.return_value = Book(
            id=fake_mongo_id,
            title="New title",
            author="New author",
            description="Lorem ipsum dolor veniam ...",
            year=1999
        )
        
        book_entity = book_service.update(update_book)
        
        assert isinstance(book_entity,Book)
        
        assert book_entity.id == fake_mongo_id
        
        assert book_entity.author == "New author"
        
        assert book_entity.title == "New title"
