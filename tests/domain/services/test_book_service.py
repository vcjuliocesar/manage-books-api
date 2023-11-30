import pytest
from typing import List
from bson import ObjectId
from mongoengine import disconnect_all
from src.domain.services.book_service import BookService
from src.domain.models.book_entity import BookEntity as Book
from src.infrastructure.configs.database import engine
from src.infrastructure.repositories.book_repository import BookRepository
from src.infrastructure.schemas.book_schema import BookSchema
from src.infrastructure.exceptions.book_already_exists_exception import BookAlreadyExistsException
from src.infrastructure.exceptions.book_not_found_exception import BookNotFoundException


@pytest.fixture(scope='function')
def mock_db():

    yield engine

    # disconnect_all()


@pytest.fixture
def test_book_repository(mock_db):

    return BookRepository(db=mock_db)


# Actúa como un proveedor de datos o recursos para las pruebas.
@pytest.fixture
def book_service(test_book_repository):

    return BookService(repository=test_book_repository)


@pytest.fixture
def set_up(book_service):

    create_book = BookSchema(
        title="Harry Potter and the Philosopher's Stone",
        author="J. K. Rowling",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        year=1997
    )

    book = book_service.create(create_book)

    yield book


def test_it_return_an_exception_if_book_already_exists(book_service, set_up):

    book = set_up

    with pytest.raises(BookAlreadyExistsException):

        create_book = BookSchema(
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )

        book_service.create(create_book)

    book_service.delete(book)


def test_it_can_create_book(book_service, set_up, caplog):

    book = set_up

    # Assert
    assert isinstance(book, Book)

    assert book.id == book.id

    assert book.title == "Harry Potter and the Philosopher's Stone"

    assert book.author == "J. K. Rowling"

    book_service.delete(book)

    captured_logs = caplog.text
    print(captured_logs)


def test_it_can_update_book(book_service, set_up):

    book_entity = set_up

    book = book_service.find_by_id(book_entity.id)

    book.author = "New author"

    book.title = "New title"

    new_book = book_service.update(book)

    assert isinstance(new_book, Book)

    assert new_book.id == book.id

    assert new_book.author == "New author"

    assert new_book.title == "New title"
    
    book_service.delete(new_book)


def test_it_can_delete_book(book_service, set_up):

    book = set_up

    try:

        book_service.delete(book)

    except:

        pytest.fail("Unexpected BookNotFoundException")


def test_it_can_find_book_by_id(book_service, set_up):

    found_book = book_service.find_by_id(set_up.id)

    assert isinstance(found_book, Book)

    assert found_book.id == set_up.id

    assert found_book.title == "Harry Potter and the Philosopher's Stone"

    assert found_book.author == "J. K. Rowling"

    assert found_book.description == "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    assert found_book.year == 1997
    
    book_service.delete(found_book)


def test_it_can_retun_all_books(book_service,set_up):

    book_1 = set_up
    
    create_book = BookSchema(
        title="Harry Potter and the Chamber of Secrets",
        author="J. K. Rowling",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        year=1999
    )

    book_2 = book_service.create(create_book)
    
    all_books = book_service.get_all()
    
    #assert isinstance(all_books, list)
    #assert len(all_books) == 2

    assert all_books[0].id == book_1.id
    assert all_books[0].title == "Harry Potter and the Philosopher's Stone"
    assert all_books[0].author == "J. K. Rowling"
    assert all_books[0].year == 1997

    assert all_books[1].id == book_2.id
    assert all_books[1].title == "Harry Potter and the Chamber of Secrets"
    assert all_books[1].author == "J. K. Rowling"
    assert all_books[1].year == 1999
    
    book_service.delete(book_1)
    
    book_service.delete(book_2)