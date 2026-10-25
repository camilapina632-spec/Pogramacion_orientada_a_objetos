from estudiantes import estudiantes

class App:
    def __init__(self):
        self.main()

    def esperarTecla(self):
        input("...¡Oprima enter para continuar!...")

    def borrarPantalla(self):
        print("\033c")
    
    def menu_acciones(self,tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
        opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n \t\tElige una Opcion: ").strip().lower()
        return opcion
    
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("accion exitosa")
        else:
            input("accion no exitosa")


    def ingresar_datos(self,tipo):
        self.borrarPantalla()
        print(f"\n\t ... Ingresar los datos del {tipo} ...")
        estudiantito={}
        estudiantito["nombre"]=input("nombre: ").upper().strip()
        estudiantito["nota"]=input("calificacion: ").upper().strip()
        return  estudiantito
    
    
    def menu_estudiante(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=self.menu_acciones("estudiante")
            match opcion:
                case '1':
                    self.borrarPantalla()
                    estudiantito=self.ingresar_datos("estudiante")
                    estudiante1=estudiantes.Estudiantes( estudiantito["nombre"], estudiantito["nota"])
                    respuesta=estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1
                case '2':
                    self.borrarPantalla()
                    id=input("Ingresa el ID del estudiante a eliminar: ")
                    respuesta=estudiantes.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)
                case '3':
                        id=input("Ingresa el ID del estudiante a modificar: ")
                        estudiantito=self.ingresar_datos("estudiante")
                        estudiante1=estudiantes.Estudiantes( estudiantito["nombre"],estudiantito["nota"])
                        respuesta=estudiante1.actualizar(id)
                        self.respuesta_sql(respuesta)
                        del estudiante1
                case '4':
                    self.borrarPantalla()
                    registros=estudiantes.Estudiantes.consultar()
                    if len(registros) >0:
                        num_estudiantes=1
                        for fila in registros:
                            print(f"Estudiante # {num_estudiantes}\n\n\t ID: {fila[0]}\n\n\t nombre: {fila[1]}\n\n\t nota: {fila[2]}")
                            num_estudiantes+=1
                            self.esperarTecla()
                    else:
                        input ("\n\t ... ¡No existen datos que mostrar por el momento!...")
                case _:
                    input("opcion invalida, vuelva a intentarlo")

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            print("menu principal")
            opcion=input("\n\t 1.-estudiante \n\t 2.-Salir \n \t\tElige una Opcion: ").strip().lower()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiante()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()   
                    print("\n\t...Salir del sistema...")
                    opcion=False
                case _:
                    input("opcion invalida, vuelva a intentarlo")


if __name__=="__main__":
    app=App()

