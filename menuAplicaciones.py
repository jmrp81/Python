print("Gestor aplicaciones Python realizadas")
salir = False

while not salir:
    print("Opciones a elegir:")
    print("1- calculadora")
    print("2- calculoMenor")
    print("3- colecciones")
    print("4- condicionales")
    print("5- diccionarios")
    print("6- factorial")
    print("7- funciones")
    print("8- operadoresRelacionales")
    print("9- tablaAnd")
    print("10- tablaMultiplicar5py")
    

    eleccion = int(input("Introducir numero de opcion\n"))

    if(eleccion == 1):
        import calculadora
    elif(eleccion == 2):
        import calculoMenor
    elif(eleccion == 3):
        import colecciones
    elif(eleccion == 4):
        import condicionales
    elif(eleccion == 5):
        import diccionarios
    elif(eleccion == 6):
        import factorial
    elif(eleccion == 7):
        import funciones
    elif(eleccion == 8):
        import operadoresRelacionales
    elif(eleccion == 9):
        import tablaAnd
    elif(eleccion == 10):
        import tablaMultiplicar5py
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
