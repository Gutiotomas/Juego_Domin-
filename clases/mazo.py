from random import randint
class Mazo():

    def __init__(self, piezas,jugador = None, numeroPiezas = 0,piezadoble = 0):
        self.numeroPiezas = numeroPiezas
        self.jugador = jugador
        self.inicia = False
        self.piezadoble = piezadoble
        self.piezas = self.generarMazo(piezas)
        self.piezasInv = self.invertirMazo(self.piezas) #generar un mazo inverso para simplificar las funciones de busqueda 
  
        
    #genera un mazo con una muestra aleatoria de 7 de la baraja original con todas las piezas
    def generarMazo(self, piezas):
        
        lista = []
        for _ in range(7):
            pieza = piezas.pop(randint(0, len(piezas)-1))
            
            #coloca de una vez la pieza 6:6 para inicializar el tablero
            if pieza == '6:6':
                self.inicia = True
            
            if pieza[0] == pieza[-1]:
                self.piezadoble += 1
            
            lista.append(pieza)
            
        return lista
    

    #invierte las piezas del mazo para simplificar como se ponen en el tablero 
    #ejemplo 5:4 ahora pasa a ser 4:5
    def invertirMazo(self,mazo):
        
        lista = []
        for i in mazo:
            lista.append(i[::-1])
        
        return lista


    
    def __str__(self):
        from clases.juego import Juego
        stringmazo= "".join([i + "\t" for i in self.piezas])
        mazoBonito = "".join([Juego.obtenerPiezaUnicode(i,1) + "\t" for i in self.piezas])
        if len(self.piezas) == 0:
            return "\n" + "".join([chr(127074) + "\t" for _ in range(3)])
        return "\n" + stringmazo + "\n" + mazoBonito
        