""" Nuevas Tecnologías - Práctica de Python
1. Crear un proyecto en Python con el nombre pypract1
2. Crear un archivo con funciones para:
    a. Imprimir el factorial de cualquier numero
    b. Mostrar los N primeros números de la serie Fibonacci
    c. Retornar el valor de la cuota de un prestamo, teniendo en cuenta que se debe especificar el valor del préstamo, número de cuotas, tasa mensual
    d. Mostrar los datos de cualquier array
    e. Mostrar los datos de cualquier diccionario
    f. Retornar el total de los pagos del diccionario dpagos= {"placa":"tis123","marca":"Aveo","pagos":[100,200,30,400], enviado como parámetro
    3. Crear un diccionario con variables
4. Crear una lista con los números del 1 al 50
5. Crear una lista con los números impares de la lista generada en el numeral 3.
6. Crear un diccionario con los datos de un vehiculo (placa, marca, modelo,valor)
7. Listar los datos del diccionario generado en el numeral 5
8. Crear una lista, con datos por teclado, que contenga las ciudades turísticas de Colombia
9. Listar las ciudades turísticas de Colombia, con base en la lista del numeral 7, en forma ordenada
10. Agregar una ciudad turística a la lista de ciudades turísticas
11. Ingresar el nombre de una ciudad y borrarla de la lista ciudades turísticas
12. Crear una clase con los datos de un vehículo """

""" num = int(input("ingrese un numero: "))

def factorial(num):
    fact = 1
    if num < 0: 
        fact = 0
    elif num == 0:
        fact = 1
    else:
        for n in range(1, num+1):
            fact = fact * n
            print(n)
    return fact


print(f"El factorial de {num} es {factorial(num)}") """

""" def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000) """

""" prestamo = int(input("Ingrese la cantidad de dinero que ha pedido prestada: "))
cuotas = int(input("Ingrese el numero de cuotas: "))

def calcularPago(prestamo, cuotas):
    pagoMensual = 0
    for c in range(1, cuotas+1):
        pagoMensual = (prestamo / cuotas) + (prestamo * 0.025)   #interes de 2.5%
        prestamo -= pagoMensual
        print(f"cuota #{c}")
        print(pagoMensual) 

calcularPago(prestamo, cuotas) """

""" my_list = [2, 5, 'DevCode', 1.2, 5]

for n in my_list:
    print(n)
 """

""" thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict) """

""" dpagos =  {"placa":"tis123","marca":"Aveo","pagos":[100,200,30,400]}

def calcularPagoTotal(dpagos):
    cuotas = dpagos["pagos"]
    acumulador = 0
    for n in cuotas:
        acumulador += n
    print(acumulador)


calcularPagoTotal(dpagos) """


""" bandName = "Wormkult"
Genre = "Death/Black metal"
Origin = "Colombia"
Year = 2017

dicWormkult = {"bandName": bandName, "Genre": Genre, "Origin": Origin, "Year": Year}

for key in dicWormkult:
  print(key, ":", dicWormkult[key]) """


""" numsOneToFifty = []

for n in range(1, 51):
    numsOneToFifty.append(n)

print(numsOneToFifty)

for n in numsOneToFifty:
    if n % 2 == 0:
        numsOneToFifty.remove(n)
print(numsOneToFifty) """


""" placa = "ABC123"
marca =  "Renault"
modelo = 2020
valor = 25000

car = {"placa": placa, "marca":marca, "modelo": modelo, "valor": valor}

for key in car:
    print(key, ":", car[key]) """

""" cities = []
flag = "y"
while flag == "y":
    city = input("Ingrese una ciudad por favor: ")
    cities.append(city)
    cities.sort()
    flag = input("Desea agregar otra ciudad (y/n)? ")
    if flag == "n":
        break

print(cities)

def borrarCiudad(ciudad):
    for city in cities:
        if city == ciudad:
            cities.remove(ciudad)
    print(cities)

ciudadBorrar = input("Ingrese la ciudad que desea eliminar de la lista: ")

borrarCiudad(ciudadBorrar) """


""" class Vehiculo:
    def __init__(self, placa, marca, modelo, precio):
        self.__Placa = placa
        self.__Marca = marca
        self.__Modelo = modelo
        self.__Precio = precio
    
    def informar(self):
        print(f"EL vehiculo tiene placas {self.__Placa}, su marca es {self.__Marca}, modelo {self.__Modelo} y tiene un valor comercial de {self.__Precio} pesos")

Vehiculo1 = Vehiculo("ABC123", "Renault", "2021", 25000)
Vehiculo1.informar() """

class Animal:
    def __init__(self, peso):
        self.Peso = peso
    
    def comer(self):
        print(f"mmmm comiendooo para aumentar el peso a mas de {self.Peso}")

class Oviparo(Animal):
    def ponerHuevos(self):
        pass

class Mamifero(Animal):
    def __init__(self, peso, sangreCaliente):
        super().__init__(peso)
        self.SangreCaliente = True

    def parir(self):
        pass

    def amamantar(self):
        pass

class Delfin(Mamifero):
    def __init__(self):
        super().__init__(peso, sangreCaliente)


a1 = Animal(60)
print(a1.Peso)

m1 = Mamifero(60, True)
print(m1.Peso)
print(m1.comer())

d1 = Delfin(50, True)
print(d1.Peso)




