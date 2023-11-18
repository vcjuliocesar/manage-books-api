from bson import ObjectId
from abc import abstractmethod,ABC
from src.domain.models.book_entity import BookEntity as Book

class BookInterface(ABC):
    
    @abstractmethod
    def create(self,book:Book) -> Book:
        pass
    
    @abstractmethod
    def find_one(self,criteria:dict) -> Book:
        pass
    
    @abstractmethod
    def find_by_id(self,id_book:ObjectId) -> Book:
        pass
    
    @abstractmethod
    def update(self,book:Book) -> Book:
        pass
    
    @abstractmethod
    def delete(self,book:Book) -> None:
        pass