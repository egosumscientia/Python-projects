#Definimos la clase
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} annos"

persona1 = Persona("Carlos", 30)
persona2 = Persona("Ana", 25)

print(persona1.presentarse())
print(persona2.presentarse())

#Encapsulamiento

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo #Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def obtener_saldo(self):
        return self.__saldo

cuenta = CuentaBancaria(5000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())

#Herencia

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad) #Llamar al constructor de la clase Persona
        self.carrera = carrera

    def presentarse(self):
        return f"Soy {self.nombre}, tengo {self.edad} annos de edad y estudio {self.carrera}"


estudiante1 = Estudiante("Luis", 20, "Ingenieria Electronica")
print(estudiante1.presentarse())

#Polimorfismo
class Gato:
    def sonido(self):
        return "Miauu"

class Perro:
    def sonido(self):
        return "Guau"

#Funcion que usa el polimorfismo
def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

hacer_sonido(gato)
hacer_sonido(perro)

print(type(gato))
print(type(perro))
