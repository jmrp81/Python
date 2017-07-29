class perimetros:
     
    def __init__(self):
        print("::::::::::::: Clase Perimetros ::::::::::::::::")
        self.menu()

    def menu(self):
        from dibujarPerimetro import dibujarPerimetro
        self.salir = False
        while not self.salir:
            print("---------------")
            print("C- cuadrado")
            print("R- rectangulo")
            print("T- triangulo")
            print("S- salir")
            opcion = input("Introducir la letra de opcion\n")
            print("---------------\n")
            
            if(opcion.lower() == "c"):
                print("Perimetro Cuadrado")
                lado = int(input("Introducir el tamaño del lado\n"))
                perimetro = lado*4
                print("Resultado del perimetro: ",perimetro)
                dibujo = dibujarPerimetro(1,lado,lado)
            elif(opcion.lower() == "r"):
                print("Perimetro Rectangulo")
                ancho = int(input("Introducir el ancho\n"))
                alto = int(input("Introducir el alto\n"))
                perimetro = (ancho*2)+(alto*2)
                print("Resultado del perimetro: ",perimetro)
            elif(opcion.lower() == "t"):
                print("Perimetro Triangulo Equilatero")
                lado = int(input("Introducir el tamaño del lado\n"))
                perimetro = lado*3
                print("Resultado del perimetro: ",perimetro)
            elif(opcion.lower() == "s"):
                print("Volviendo anterior .....")
                from Principal import principal
                principal1 = principal()
            else:
                print("Opcion incorrecta")
                
