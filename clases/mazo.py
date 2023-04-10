from random import randint
class Mazo():
    def __init__(self, piezas, numeroPiezas = 0):
        self.numeroPiezas = numeroPiezas
        self.piezas = self.generarMazo(piezas)
        self.inicia = False
    
    def generarMazo(self, piezas):
        lista = []
        for i in range(7):
            pieza = piezas.pop(randint(0, len(piezas)-1))
            if pieza == "6:6":
                self.inicia = True
            lista.append(pieza)
        return lista
    
    def __str__(self):
        return f"{self.piezas} {self.inicia}"
        