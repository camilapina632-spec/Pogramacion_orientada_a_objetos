"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
def area_rectangulo(base, altura):
    return base * altura

print(area_rectangulo(5,3))

#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base * self.altura

rect = Rectangulo(5,3)
print(rect.area())

class Rectangulos:
    def area (self, base, altura):
        areaR=base*altura
        return areaR

Rectangulo1= Rectangulos() #Crear o instanciar un objeto "rectangulo1" de la clase "Rectangulos"
print(f"El area del rectangulo es: {Rectangulos.area(5, 6)}")

#Cuando no se usa un metodo constructor no se coloca nada para indicar wur no existe tal metodo, en caso de que se use un metoo ya muestra dichos valores.
# 
