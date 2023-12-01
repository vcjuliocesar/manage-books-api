from mongoengine import connect
from src.infrastructure.configs.enviroment import get_enviroment_settinngs

env = get_enviroment_settinngs()

engine = connect(
            db = env().DATABASE_NAME,
            username = env().DATABASE_USER,
            password = env().DATABASE_PASSWORD,
            host = env().DATABASE_HOST,
            port = env().DATABASE_PORT,
            uuidRepresentation="standard"
        )

def db_connect():

    yield engine
