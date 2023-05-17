"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Carro:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return (f"\nLa informacion del Carro es: \n"
                f"Marca del Carro: {self.marca}\n"
                f"Modelo del Carro: {self.modelo}\n"
                f"Color del Carro: {self.color}\n")


# clase 02
class Colegio:
    def __init__(self, nombre, numProfesores, numAlumnos, presupuesto):
        self.nombre = nombre
        self.numProfesores = numProfesores
        self.numAlumnos = numAlumnos
        self.presupuesto = presupuesto

    def __str__(self):
        return (f"\nDatos del colegio \"{self.nombre}\":\n"
                f"Cuenta con {self.numProfesores} profesores\n"
                f"Cuenta con {self.numAlumnos} alumnos\n"
                f"Tiene un presupuesto otorgado por el estado de ${self.presupuesto} dolares")
