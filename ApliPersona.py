from Persona import persona
print("Vamos a crear pesonas")
salir = False
while not salir:
    nombre = input("Introduce el nombre de la persona\n")
    edad = input("Introduce la edad\n")
    direccion = input("Introduce la direccion\n")
    persona1 = persona(nombre,edad,direccion)

    v_nombre = persona1.getNombre()
    print("su edad es ",v_nombre)

    opcion = input("desea salir (si o no)\n")
    if(opcion.lower() == "si"):
        salir = True
        print("Gracias por usar el programa")
        break
    elif(opcion.lower() == "no"):
        salir = False
    else:
        print("Introducida opcion incorrecta")
