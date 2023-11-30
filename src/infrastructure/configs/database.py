from mongoengine import connect, disconnect
# from mongoengine.connection import disconnect

engine = connect(
            db="manage-books-api",
            host="localhost",
            port=27017
        )

def db_connect():

    try:
        
        yield engine

    finally:

        disconnect()
