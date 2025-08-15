# Programación orientada a objetos
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def saludar(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y vivo en {self.ciudad}.")

persona2 = Persona("juan", 30, "Bogotá")