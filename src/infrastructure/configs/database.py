from mongoengine import connect

def db_connect():
    return connect(
        db="manage-books-api",
        host="localhost",
        port=27017
)
