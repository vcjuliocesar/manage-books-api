import json
from bson import ObjectId
from fastapi import HTTPException,APIRouter,Depends,status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.app.usecases.book.create_book_use_case import CreateBookUseCase
from src.app.usecases.book.find_by_id_book_use_case import FindByIdBookUseCase
from src.app.usecases.book.update_book_use_case import UpdateBookUseCase
from src.infrastructure.schemas.book_schema import BookSchema,BookPostRequest
from src.infrastructure.exceptions.book_already_exists_exception import BookAlreadyExistsException
from src.infrastructure.exceptions.book_not_found_exception import BookNotFoundException
from src.infrastructure.exceptions.get_http_exception import get_http_exception

book_router = APIRouter(prefix="/api/v1",tags=["Books"])

@book_router.post("/books",response_model=BookSchema,status_code=status.HTTP_200_OK)
async def create(book:BookPostRequest,use_case:CreateBookUseCase = Depends()):
    
    try:
        
        use_case.execute(book)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":f"Book {book.title} created"})
        
    except BookAlreadyExistsException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content={"message":f"{str(error)}"})

@book_router.get("/books/{id_book}",response_model=BookSchema,status_code=status.HTTP_200_OK)
async def find_by_id(id_book:str,use_case:FindByIdBookUseCase = Depends()):
    
    try:
        
        result = use_case.execute(ObjectId(id_book))
        
        return JSONResponse(status_code=status.HTTP_200_OK,content=json.loads(result))
    
    except BookNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content={"message":f"{str(error)}"})

@book_router.put("/books/",response_model=BookSchema,status_code=status.HTTP_200_OK)
async def update(id_book:str,book:BookPostRequest,use_case:UpdateBookUseCase = Depends()):
    
    try:
        
        use_case.execute(ObjectId(id_book),book)
        
        return JSONResponse(status_code=status.HTTP_200_OK,content={"message":f"Book {id_book} updated"})
    
    except BookNotFoundException as error:
        
        raise get_http_exception(error)
    
    except Exception as error:
        
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,content={"message":f"{str(error)}"})
    
    