from bson import InvalidDocument, ObjectId


class OID(str):
    # Este método de clase especial se utiliza para proporcionar validadores para el campo OID. Específicamente, se usa en conjunción con Pydantic para validar datos.
    @classmethod
    def __get_validators__(cls):

        yield cls.validate

    @classmethod
    def validate(cls, v):

        try:

            return ObjectId(str(v))

        except InvalidDocument:

            raise ValueError("Not a valid ObjectId")
