from bson import InvalidDocument, ObjectId


class OID(str):
    # Este método de clase especial se utiliza para proporcionar validadores para el campo OID. Específicamente, se usa en conjunción con Pydantic para validar datos.
    @classmethod
    def __get_validators__(cls):

        yield cls.validate

    @classmethod
    def validate(cls, v):

        if not isinstance(v, ObjectId):
            raise ValueError('Not a valid ObjectId')
        return str(v)

    # @classmethod
    # def __get_pydantic_core_schema__(cls):
    #     return {
    #         "type": "string",  # Ejemplo de cómo podrías definir el esquema JSON
    #         "format": "objectid"
    #         # Puedes ajustar este esquema para que se adapte a tus necesidades
    #     }