from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id, usuario, contrasenna, correo, numero, fecha_nacimiento FROM public."usuario" """)
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuarios.append(usuario.to_JSON())

            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_usuario(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT id, usuario, contrasenna, correo, numero, fecha_nacimiento FROM public."usuario" WHERE id = %s""", (id,))
                row = cursor.fetchone()

                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuario = usuario.to_JSON()

            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public."usuario" (usuario, contrasenna, correo, numero, fecha_nacimiento)
                            VALUES (%s, %s, %s, %s, %s)""", (usuario.usuario, usuario.contrasenna, usuario.correo, usuario.numero, usuario.fecha_nacimiento))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE public."usuario" SET usuario = %s, contrasenna = %s, correo = %s, numero = %s, fecha_nacimiento =%s  
                                WHERE id = %s""", (usuario.id, usuario.usuario, usuario.contrasenna, usuario.correo, usuario.numero, usuario.fecha_nacimiento))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM public."usuario" WHERE id = %s""", (usuario.id,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)