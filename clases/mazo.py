from random import randint
class Mazo():

    def __init__(self, piezas,jugador = None, numeroPiezas = 0,piezadoble = 0):
        self.numeroPiezas = numeroPiezas
        self.jugador = jugador
        self.inicia = False
        self.piezadoble = piezadoble
        self.piezas = self.generarMazo(piezas)
        self.piezasInv = self.invertirMazo(self.piezas)
        
    
    def generarMazo(self, piezas):
        
        lista = []
        for _ in range(7):
            pieza = piezas.pop(randint(0, len(piezas)-1))
            
            if pieza == '6:6':
                self.inicia = True
            
            if pieza[0] == pieza[-1]:
                self.piezadoble += 1
            
            lista.append(pieza)
            
        return lista
    
    def invertirMazo(self,mazo):
        
        lista = []
        for i in mazo:
            lista.append(i[::-1])
        
        return lista


    
    def __str__(self):
        return f"{self.piezas}"
        