from fastapi import FastAPI
from src.domain.models.base_entity import init
from mongoengine import Document, StringField


app = FastAPI()

class MiModelo(Document):
    nombre = StringField(required=True)
    # Define los campos que necesites para tu colección
    
@app.get("/")
async def read_root():
    # Ejemplo de uso de MongoEngine
    objeto = MiModelo(nombre="Ejemplo")
    objeto.save()  # Guardar el objeto en la base de datos
    return {"message": "Objeto guardado en MongoDB"}

@app.get("/consulta")
async def read_data():
    # Consultar datos en la colección
    objetos = MiModelo.objects().all()
    return {"message": "Datos consultados", "data": objetos}

init()