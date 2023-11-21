class BookNotFoundException(Exception):
    
    def __init__(self, message:str="Book not foud") -> None:
        
        self.message = message
        
        super().__init__(self.message)