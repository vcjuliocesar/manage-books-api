class BookAlreadyExistsException(Exception):
    
    def __init__(self, message:str = "Book already exists") -> None:
        
        self.message = message
        
        super().__init__(self.message)