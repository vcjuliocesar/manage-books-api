import pytest
from fastapi.testclient import TestClient
from fastapi import status
from src.domain.services.book_service import BookService
from src.infrastructure.configs.database import engine
from src.infrastructure.repositories.book_repository import BookRepository
from src.infrastructure.schemas.book_schema import BookSchema
from src.app.main import app


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
def client() -> TestClient:
    
    return TestClient(app)

@pytest.fixture
def set_up(client:TestClient):
     pass
    

def test_it_can_create_a_book(client:TestClient,book_service):
    
    response = client.post("/api/v1/books",json={
        "title":"Harry Potter and the Philosopher's Stone",
        "author":"J. K. Rowling",
        "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "year":1997
    })
    
    assert response.status_code == status.HTTP_200_OK
    