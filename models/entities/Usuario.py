from utils.DateFormat import DateFormat

class Usuario():

    def __init__(self, id, usuario=None, contrasenna=None, correo=None, numero=None,fecha_nacimiento=None) -> None:
        self.id = id
        self.usuario = usuario
        self.contrasenna = contrasenna
        self.correo = correo
        self.numero = numero
        self.fecha_nacimiento = fecha_nacimiento

    def to_JSON(self):
        return {
            'id': self.id,
            'usuario': self.usuario,
            'contrasenna': self.contrasenna,
            'correo': self.correo,
            'numero': self.numero,
            'fecha_nacimiento': DateFormat.convert_date(self.fecha_nacimiento)
            }