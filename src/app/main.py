from fastapi import FastAPI
from src.domain.models.base_entity import init
from src.app.routers.api.book import book_router


app = FastAPI()

app.include_router(book_router)

init()
