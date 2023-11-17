import pytest
from src.domain.services.book_service import BookService
from src.domain.models.book_entity import BookEntity, BookEntity as Book
from src.infrastructure.schemas.book_schema import BookSchema
from src.infrastructure.exceptions.book_already_exists_exception import BookAlreadyExistsException


@pytest.fixture
def book_service():
    return BookService()

def test_it_return_an_exception_if_book_already_exists(book_service):

    book=book_service.create(BookSchema(
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        ))

    with pytest.raises(BookAlreadyExistsException):

        create_book = BookSchema(
            title="Harry Potter and the Philosopher's Stone",
            author="J. K. Rowling",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            year=1997
        )

        book_service.create(create_book)
        
    Book.objects.get(id=book.id).delete()


def test_it_can_create_book(book_service):
    
    # Arrange
    create_book = BookSchema(
        title="Harry Potter and the Philosopher's Stone",
        author="J. K. Rowling",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        year=1997
    )

    # Act
    book_entity = book_service.create(create_book)
    
    # Assert
    assert isinstance(book_entity, BookEntity)

    assert book_entity.title == "Harry Potter and the Philosopher's Stone"

    assert book_entity.author == "J. K. Rowling"

    Book.objects.get(id=book_entity.id).delete()