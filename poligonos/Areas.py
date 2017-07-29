class areas:
   
    def __init__(self):
        print("::::::::::::: Clase Areas ::::::::::::::::")
        self.menu()

    def menu(self):
        from dibujarArea import dibujarArea
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
                print("Area Cuadrado")
                lado = int(input("Introducir el tamaño del lado\n"))
                area = lado*lado
                print("Resultado del area: ",area)
                dibujo = dibujarArea(1,lado,lado)
            elif(opcion.lower() == "r"):
                print("Area Rectangulo")
                ancho = int(input("Introducir el ancho\n"))
                alto = int(input("Introducir el alto\n"))
                area = ancho*alto
                print("Resultado del area: ",area)
                dibujo = dibujarArea(2,ancho,alto)
            elif(opcion.lower() == "t"):
                print("Area Triangulo")
                base = int(input("Introducir el tamaño de la base\n"))
                altura = int(input("Introducir el tamaño de la altura\n"))
                area = (base*altura)/2
                print("Resultado del area: ",area)
                dibujo = dibujarArea(2,base,0)
            elif(opcion.lower() == "s"):
                print("Volviendo anterior .....")
                from Principal import principal
                principal1 = principal()
            else:
                print("Opcion incorrecta")   

