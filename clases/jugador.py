from random import random,randint
from clases.jugada import Jugada

class Jugador():
    def __init__(self, tipo,mazo):
        self.mazo = mazo
        self.tipo = tipo
        self.ganador = False
    
    
    def realizarJugadaM(self):
        #if random()>=0.9: #arreglar para introducirle un nivel de "inteligencia"
        #    Jugada("PASAR",None)
        #    return "paso"
        posibleJugada = self.buscarCoincidencia(self.mazo)

        if posibleJugada == ([],[]):
            Jugada("PASAR",None)
            return "paso"
        
        if random()<=0.5 and posibleJugada[0]!= []: 
            cabeza =  posibleJugada[0][randint(0,len(posibleJugada[0])-1)]
            maquina = Jugada("PONER",cabeza)
            maquina.colocarPieza(self.mazo,0)
            return f"{self.tipo} ha puesto la pieza {cabeza}"
        elif posibleJugada[-1]!= []:
            cola =  posibleJugada[-1][randint(0,len(posibleJugada[-1])-1)]
            maquina = Jugada("PONER",cola)
            maquina.colocarPieza(self.mazo,-1)
            return f"{self.tipo} ha puesto la pieza {cola}"
        else:
            Jugada("PASAR",None)
            return "paso"
    

    def realizarJugadaH(self,accion,pieza):
        # hacer la jugada mediante entradas humanas
        #Jugada(accion,pieza) 
        #accion -> 0 = poner, 1 = Pasar
        #pieza numero entre 0 y longitud -1 del mazo
        pass

    def buscarCoincidencia(self,mazo):
        from clases.juego import Juego

        NewCabeza = []
        NewCola = []
        primera, ultima = Juego.RegistroJugadas[0][0],Juego.RegistroJugadas[-1][-1]
        for pieza in range(len(mazo.piezas)):
            if mazo.piezas[pieza][-1] == primera:
                NewCabeza += [mazo.piezas[pieza]]
            if mazo.piezas[pieza][0] == ultima:
                NewCola += [mazo.piezas[pieza]]
            if mazo.piezasInv[pieza][-1] == primera:
                NewCabeza += [mazo.piezasInv[pieza]]
            if mazo.piezasInv[pieza][0] == ultima:
                NewCola += [mazo.piezasInv[pieza]]
        return NewCabeza,NewCola


    def __str__(self):
        return f"{self.tipo} {self.mazo}"
    
        if self.tipo[0] == "H":
            return f"{self.tipo} {self.mazo}"
        else:
            return f"{self.tipo} {len(self.mazo.piezas)}"
