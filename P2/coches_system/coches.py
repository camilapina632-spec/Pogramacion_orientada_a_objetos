from conexionBD import conexion,cursor

class Coches:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._asientos=asientos

    def acelerar(self):
        self._velocidad+=1

    def frenar(self):
        self._velocidad-=1

    @property
    def velocidad(self):
            return self._velocidad
    @property
    def getMarca(self):
            return self._marca
    @property
    def color(self):
            return self._color
    @property
    def modelo(self):
            return self._modelo
    @property
    def marca(self,marca):
         self._marca=marca
    @property
    def asientos(self):
            return self._asientos
    @property
    def potencia(self):
            return self._potencia
   
    @modelo.setter
    def modelo(self,modelo):
         self._modelo=modelo
    @potencia.setter
    def potencia(self,potencia):
         self._potencia=potencia
    @velocidad.setter
    def setVelocidad(self,velocidad):
         self._velocidad=velocidad
    @asientos.setter
    def asientos(self,asientos):
         self._asientos=asientos
    @color.setter
    def color(self,color):
         self._color=color

    def insertar(self):
        try:
            cursor.execute("insert into coches values (NULL,%s,%s,%s,%s,%s,%s)",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos))
            conexion.commit()
            return True
        except:
             return False
    @staticmethod
    def consultar():
        try:
             cursor.execute("select * from coches,")
             return cursor.fetchall
        except:
             return[]

    @staticmethod
    def eliminar(self,id):
            try:
                 cursor.execute("delete from coches where id=%s",(id,))
                 conexion.commit()
                 return True
            except:
                 return False

    def actualizar(self,id):
            try:
                 cursor.execute("update coches set marca=%s,color=%s,modelo=%s,velocidad=%s,potencia=%s,asientos=%s where od=%s",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos, id))
                 conexion.commit()
                 return True
            except:
                 False

 