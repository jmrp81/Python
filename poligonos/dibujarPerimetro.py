class dibujarPerimetro:
    
    def __init__(self,tipo,ancho,alto):
        from Perimetros import perimetros
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        print("::::::::::::: Imagen Perimetro ::::::::::::::::")
        if(self.tipo==1):#cuadrado
            matriz = [] 

            for i in range(ancho): 
                matriz.append([0]*ancho) 

            for f in range(ancho):
                salida=""
                for c in range(ancho): 
                    matriz[f][c] = "* "
                    if((f==0 or (f==ancho-1))or((c==0 or (c==ancho-1)))):
                        print(matriz[f][c],end='')
                    else:
                        print("  ",end='')
                print("")
            perimetros = perimetros()
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
            perimetros = perimetros()
        elif(self.tipo==3):#triangulo
            print("No se puede dibujar, error en tipo de objeto")
