from coches import coches
from camiones import camiones

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
        cochesitos={}
        cochesitos["marca"]=input("Ingrese la marca: ").upper().strip()
        cochesitos["color"]=input("Ingrese el color: ").upper().strip()
        cochesitos["modelo"]=input("Ingrese el modelo: ").upper().strip()
        cochesitos["velocidad"]=int(input("Ingrese la vlocidad maxima: "))
        cochesitos["potencia"]=int(input("Ingrese la potencia: "))
        cochesitos["asientos"]=int(input("Ingrese el numero de asientos: "))
        return cochesitos
    

    def menu_coche(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=self.menu_acciones("Coches")
            match opcion:
                case '1':
                    #crear objetos de la clase Coches
                    self.borrarPantalla()
                    cochesitos=self.ingresar_datos("Coches")
                    coche1=coches.Coches(cochesitos["marca"],cochesitos["color"],cochesitos["modelo"],cochesitos["velocidad"],cochesitos["potencia"], cochesitos["asientos"])
                    respuesta=coche1.insertar()
                    self.respuesta_sql(respuesta)
                    del coche1
                case '2':
                    self.borrarPantalla()
                    coche1=coches.Coches('','','',0,0,0)
                    id=input("Ingresa el ID del coche a eliminar: ")
                    respuesta=coche1.eliminar(id)
                    self.respuesta_sql(respuesta)
                    del coche1
                case '3':
                    id=input("Ingresa el ID del coche a modificar: ")
                    cochesitos=self.ingresar_datos("Coches")
                    coche1=coches.Coches(cochesitos["marca"],cochesitos["color"],cochesitos["modelo"],cochesitos["velocidad"],cochesitos["potencia"], cochesitos["asientos"])
                    respuesta=coche1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coche1
                case '4':
                    self.borrarPantalla()
                    coche1=coches.Coches('','','',0,0,0)
                    registros=coche1.consultar()
                    if len(registros) >0:
                        num_coches=1
                        for fila in registros:
                            print(f"Coche # {num_coches}\n\n\t ID: {fila[0]}\n\n\t marca: {fila[1]}\n\n\t color: {fila[2]},\n\n\t modelo: {fila[3]},\n\n\t velocidad: {fila[4]},\n\n\t potencia: {fila[5]}\n\n\t asientos: {fila[6]}")
                            num_coches+=1
                            self.esperarTecla()
                    else:
                        input ("\n\t ... ¡No existen datos que mostrar por el momento!...")
                case _:
                    input("opcion invalida, vuelva a intentarlo")

    def menu_camiones(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=self.menu_acciones("Camiones")
            match opcion:
                case '1':
                    #crear objetos de la clase Camiones
                    self.borrarPantalla()
                    camioncitos=self.ingresar_datos("Camiones")
                    eje=input("Ingrese el numero de ejes del camion: ")
                    capacidadCarga=input("Ingrese la capacidad de carga del camion: ")
                    camion1=camiones.Camiones(camioncitos["marca"],camioncitos["color"],camioncitos["modelo"],camioncitos["velocidad"],camioncitos["potencia"], camioncitos["asientos"],eje,capacidadCarga)
                    respuesta=camion1.insertar()
                    self.respuesta_sql(respuesta)
                    del camion1
                case '2':
                    self.borrarPantalla()
                    camion1=camiones.Camiones('','','',0,0,0,'','')
                    id=input("Ingresa el ID del camion a eliminar: ")
                    respuesta=camion1.eliminar(id)
                    self.respuesta_sql(respuesta)
                    del camion1
                case '3':
                    id=input("Ingresa el ID del camion a modificar: ")
                    camioncitos=self.ingresar_datos("Camiones")
                    eje=input("Ingrese el numero de ejes del camion: ")
                    capacidadCarga=input("Ingrese la capacidad de carga del camion: ")
                    camion1=camiones.Camiones(camioncitos["marca"],camioncitos["color"],camioncitos["modelo"],camioncitos["velocidad"],camioncitos["potencia"], camioncitos["asientos"],eje,capacidadCarga)
                    respuesta=camion1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del camion1
                case '4':
                    self.borrarPantalla()
                    camion1=camiones.Camiones('','','',0,0,0,'','')
                    documentos=camion1.consultar()
                    if len(documentos) >0:
                        num_camiones=1
                        for fila in documentos:
                            print(f"Camion # {num_camiones}\n\n\t ID: {fila[0]}\n\n\t marca: {fila[1]}\n\n\t color: {fila[2]},\n\n\t modelo: {fila[3]},\n\n\t velocidad: {fila[4]}")
                            num_camiones+=1
                    else:
                        print("No hay camiones registrados.")
                    self.esperarTecla()
                case _:
                    input("opcion invalida, vuelva a intentarlo")
   
    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            print("menu principal")
            opcion=input("\n\t 1.-Coches \n\t 2.-Salir \n \t\tElige una Opcion: ").strip().lower()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coche()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()
                    self.menu_camiones()
                    self.esperarTecla()
                case '3':
                    self.borrarPantalla()
                    print("\n\t...Salir del sistema...")
                    opcion=False
                case _:
                    self.borrarPantalla()
                    input("opcion invalida, vuelva a intentarlo")

    
if __name__=="__main__":
    app=App()

