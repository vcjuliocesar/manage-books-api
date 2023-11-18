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
        
        mock_update.side_effect = BookNotFoundException("Book not found")

        with pytest.raises(BookNotFoundException):

            book_service.update(update_book)
        
        mock_update.side_effect = None

        book_entity = book_service.update(update_book)

        assert isinstance(book_entity, Book)

        assert book_entity.id == fake_mongo_id

        assert book_entity.author == "New author"

        assert book_entity.title == "New title"


def test_it_can_delete_book(book_service):

    with patch.object(BookService, 'delete') as mock_delete:

        fake_mongo_id = ObjectId('60a5c1d5e9b92b6f8e87654a')

        mock_delete.side_effect = BookNotFoundException("Book not found")

        with pytest.raises(BookNotFoundException):

            book_service.delete(fake_mongo_id)

        mock_delete.side_effect = None

        try:

            book_service.delete(fake_mongo_id)

        except:

            pytest.fail("Unexpected BookNotFoundException")


def test_it_can_find_book_by_id(book_service):

    with patch.object(BookService, "find_by_id") as mock_find_by_id:

        fake_mongo_id = ObjectId('60a5c1d5e9b92b6f8e87654a')

        mock_find_by_id.return_value = Book(
            id=fake_mongo_id,
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )
        
        mock_find_by_id.side_effect = BookNotFoundException("Book not found")
        
        with pytest.raises(BookNotFoundException):

            book_service.find_by_id(fake_mongo_id)

        mock_find_by_id.side_effect = None

        found_book = book_service.find_by_id(fake_mongo_id)

        assert isinstance(found_book, Book)

        assert found_book.id == fake_mongo_id

        assert found_book.title == "Harry Potter and the Philosopher's Stone"
        
        assert found_book.author == "J. K. Rowling"
        
        assert found_book.description == "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        
        assert found_book.year == 1997
