
from mis_clases import Carro

# Crear dos objetos de la clase 01

# objeto 01

# crear

c = Carro("Toyota", "Toyota 2021", "Negra")

# Presentar objeto; usar el método __st__
print(c)
# objeto 02



# crear ingresando valores por teclado

marca = input("\nIngrese la marca del carro: ")
modelo = input("Ingrese el modelo del carro: ")
color = input("Ingrese el color del carro: ")

cD = Carro(marca, modelo, color)

# Presentar objeto; usar el método __st__

print(cD)

