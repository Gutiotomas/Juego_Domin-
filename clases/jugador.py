from random import random,randint
from clases.jugada import Jugada

class Jugador():
    
    def __init__(self, tipo,mazo):
        self.mazo = mazo
        self.tipo = tipo
        self.ganador = False
    
    
    def realizarJugadaM(self):
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
    

    def realizarJugadaH(self,accion,indexPieza,pos):
        if accion != 0 and accion != 1:
            return "jugada invalida"

        if accion == 1:
            Jugada("PASAR",None)
            return "paso"
        
        if indexPieza>=len(self.mazo.piezas):
            return "jugada invalida"

        if pos !=0 and pos!=1:
            return "jugada invalida"

        piezaEnMazo = self.mazo.piezas[indexPieza]

        jugada,pieza,tipo = Jugada.probarJugada(piezaEnMazo,pos)
        
        if not jugada:
            return "jugada invalida"
        
        J = Jugada("PONER",pieza)
        J.colocarPieza(self.mazo,tipo) 
        return f"{self.tipo} ha puesto la pieza {pieza}"  


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
