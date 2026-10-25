from conexionbD import cursor,conexion

class Estudiantes:
    def __init__(self,nombre,nota):
        self._nombre=nombre
        self._nota=nota

    @property
    def nombre(self):
        return self._nombre

    @property
    def nota(self):
        return self._nota

    @nombre.setter
    def nombre(self, nombre):
        self._nombre

    @nota.setter
    def nota(self,nota):
        self._nota

    def insertar(self):
        try:
            cursor.execute("insert into estudiante values (NULL,%s,%s)",(self._nombre,self._nota))
            conexion.commit()
            return True
        except:
             return False

    @staticmethod
    def consultar():
        try:
             cursor.execute("select * from estudiante")
             return cursor.fetchall()
        except:
             return[]

    @staticmethod
    def eliminar(id):
            try:
                 cursor.execute("delete from estudiante where id=%s",(id,))
                 conexion.commit()
                 return True
            except:
                 return False

    def actualizar(self, id):
        try:
            cursor.execute(
                "UPDATE estudiante SET nombre=%s, nota=%s WHERE id=%s",
                (self._nombre, self._nota, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("Error al actualizar:", e)
            return False

 