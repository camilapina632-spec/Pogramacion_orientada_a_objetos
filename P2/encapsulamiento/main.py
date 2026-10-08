#Programa principal desde la que se manda llamar los objetos de la clase de coches
from coches import Coches

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

for i in range (1,101):
    coche1.acelerar()
print (coche1.getVelocidad())

coche1.setVelocidad(400)
print (coche1.getVelocidad())