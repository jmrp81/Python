print("programa menor")

numero1=int(input("introduce el numero 1\n"))
numero2=int(input("introduce el numero 2\n"))
numero3=int(input("introduce el numero 3\n"))

print("Comprobando el menor ........")

print("Nuemeros introducidos ",numero1," - ",numero2," - ",numero3)
 
if((numero1<numero2) and (numero2<numero3)):
    print("El ",numero1," es el menor")
elif((numero2<numero1) and (numero1<numero3)):
    print("El ",numero2," es el menor")
elif((numero3<numero2) and (numero2<numero1)):
    print("El ",numero3," es el menor")
