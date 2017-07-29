class dibujarArea:
    
    def __init__(self,tipo,ancho,alto):
        from Areas import areas
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        print("::::::::::::: Imagen Area ::::::::::::::::")
        if(self.tipo==1):#cuadrado
            matriz = [] 

            for i in range(ancho): 
                matriz.append([0]*ancho) 

            for f in range(ancho):
                salida=""
                for c in range(ancho): 
                    matriz[f][c] = "* "
                    print(matriz[f][c],end='')
                print("")
            areas = areas()
        elif(self.tipo==2):#rectangulo
            matriz = [] 

            for i in range(alto): 
                matriz.append([0]*ancho) 

            for f in range(alto):
                salida=""
                for c in range(ancho): 
                    matriz[f][c] = "* "
                    print(matriz[f][c],end='')
                print("")
            areas = areas()
            areas = areas()
        elif(self.tipo==3):#triangulo
                
            areas = areas()
        else:
            print("No se puede dibujar, error en tipo de objeto")
