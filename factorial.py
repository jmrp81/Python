print("Factorial de un numero ")
salir = False

while not salir:
    numero1 = int(input("introduce el numero\n"))
    tipo = input("introducir la opcion usada: for o while\n")

    if(tipo.lower() == "for"):
        print("\nFactorial con for")
        for elemento in range(1,numero1):
            numero1=numero1*elemento
    elif(tipo.lower() == "while"):
        print("\nFactorial con while")
        contador = numero1 -1
        while contador > 0:
            numero1 = numero1*contador
            contador = contador -1
    print("factorial ",numero1)

    opcion = input("desea salir (si o no)\n")
    if(opcion.lower() == "si"):
        salir = True
        prrint("Gracias por usar el programa")
        break
    elif(opcion.lower() == "no"):
        salir = False
    else:
        print("Introducida opcion incorrecta")
