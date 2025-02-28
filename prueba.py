import random

class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
            return f"Persona('{self.nombre}', {self.edad})"


def generar_lista(n):
    lista= []
    for i in range(n):
      edad_aleatoria= random.randint(1,10)
      Persona1= Persona("mario", edad_aleatoria)
      lista.append(Persona1)
    return lista

print(generar_lista(10))

def saludar():
  lista2 = generar_lista(10)
  for i in range(10):
    if i > i-1:
      return "hola"

print(saludar())
