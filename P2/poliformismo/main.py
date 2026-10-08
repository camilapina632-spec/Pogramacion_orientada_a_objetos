#Programa principal desde la que se manda llamar los objetos de la clase de coches
from coches import *

coche1=Coches(
    marca="VW",
    color="Blanco",
    modelo= "2022",
    velocidad=220,
    potencia=150,
    asientos=5
)

coche2=Coches(
    marca="Nissan",
    color="Azul",
    modelo="2020",
    velocidad=180,
    potencia=150,
    asientos=6
)

camion1=Camiones( "Dina","Negro", "2020", 180, 300, 12, 8, 2500)
camion2=Camiones( "Star","Azul", "2019", 150, 200, 14, 6 , 2000)

camioneta1=Camionetas( "Renault","Amarillo", "2025", 240, 250, 8, "delantera", True)
camioneta2=Camionetas( "Nissan","Blanca", "2020", 180, 150, 6, "trasera", False)


for i in range (1,101):
    coche1.acelerar()
print (coche1.getVelocidad())

coche1.setVelocidad(400)
print (coche1.getVelocidad())