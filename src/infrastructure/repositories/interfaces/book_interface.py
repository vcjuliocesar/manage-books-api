from abc import abstractmethod,ABC
from src.domain.models.book_entity import BookEntity as Book

class BookInterface(ABC):
    
    @abstractmethod
    def create(self,book:Book) -> Book:
        pass