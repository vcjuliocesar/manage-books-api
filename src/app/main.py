from fastapi import FastAPI
from src.domain.models.base_entity import init
from src.app.routers.api.book import book_router
from src.infrastructure.configs.enviroment import get_enviroment_settinngs
from src.infrastructure.exceptions.error_handler import ErrorHandler

env = get_enviroment_settinngs()

app = FastAPI()

app.title = env().APP_NAME

app.version = env().API_VERSION

app.description = env().APP_DESCRIPTION

app.add_middleware(ErrorHandler)

app.include_router(book_router)

init()

print("Pr no activity")