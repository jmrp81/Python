print("calculadora con funciones")
salir = False

while not salir:
    print("Opciones calculadora")
    print("1- cuadrado primer numero")
    print("2- suma")
    print("3- resta")
    print("4- multiplicacion")
    print("5- division")
    print("6- factorial primer numero")

    numero1=int(input("Introducir el primer numero\n"))
    numero2=int(input("Introducir el segundo numero\n"))
    
    eleccion = int(input("Introducir numero de opcion\n"))

    if(eleccion == 1):
        print(cuadrado(numero1,numero2))
    elif(eleccion == 2):
        print(suma(numero1,numero2))
    elif(eleccion == 3):
        print(resta(numero1,numero2))
    elif(eleccion == 4):
        print(multiplicacion(numero1,numero2))
    elif(eleccion == 5):
        print(division(numero1,numero2))
    elif(eleccion == 6):
        print(factorial(numero1))
    else:
        print("Opcion incorrecta")
    
    opcion = input("desea salir (si o no)\n")
    if(opcion.lower() == "si"):
        salir = True
        print("Gracias por usar el programa")
        break
    elif(opcion.lower() == "no"):
        salir = False
    else:
        print("Introducida opcion incorrecta")


def cuadrado(param1):
    resultado = param1 * param1
    return resultado

def suma(param1,param2):
    resultado = param1+param2
    return resultado

def resta(param1,param2):
    resultado = param1-param2
    return resultado

def multiplicacion(param1,param2):
    resultado = param1*param2
    return resultado

def division(param1,param2):
    resultado = param1/param2
    return resultado

def factorial(param1):
    tipo = input("introducir la opcion usada: for o while\n")
    if(tipo.lower() == "for"):
        return factorialFor(param1)
    elif(tipo.lower() == "while"):
        return factorialWhile(param1)

def factorialFor(param1):
    for elemento in range(1,numero1):
        numero1=numero1*elemento
        return numero1

def factorialWhile(param1):
    contador = numero1 -1
    while contador > 0:
        numero1 = numero1*contador
        contador = contador -1
        return numero1










    
