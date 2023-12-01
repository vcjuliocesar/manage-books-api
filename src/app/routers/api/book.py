from fastapi import HTTPException,APIRouter,Depends,status
from fastapi.responses import JSONResponse
from src.app.usecases.book.create_book_use_case import CreateBookUseCase
from src.infrastructure.schemas.book_schema import BookSchema,BookPostRequest

book_router = APIRouter(prefix="/api/v1",tags=["Books"])

@book_router.post("/books",response_model=BookSchema,status_code=status.HTTP_200_OK)
async def create(book:BookPostRequest,use_case:CreateBookUseCase = Depends()):
    
    try:
        
        use_case.execute(book)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":f"Book {book.title} created"})
        
    except Exception as error:
        
        raise error