from Areas import areas
from Perimetros import perimetros
class principal:
        
    def __init__(self):
        print("::::::::::::: Clase Principal ::::::::::::::::")
        self.menu()

    def menu(self):
        self.salir = False
        while not self.salir:
            print("---------------")
            print("A- areas")
            print("P- perimetros")
            print("S- salir")       
            opcion = input("Introducir la letra de opcion\n")
            print("---------------\n")
            if(opcion.lower() == "a"):               
                area = areas()
            elif(opcion.lower() == "p"):           
                perimetro = perimetros()
            elif(opcion.lower() == "s"):
                self.salir = True
                print("Gracias por usar el programa")
            else:
                print("Opcion incorrecta")

        
apli = principal()
