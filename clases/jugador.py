from random import random,randint
from clases.jugada import Jugada

class Jugador():
    
    def __init__(self, tipo,mazo):
        self.mazo = mazo
        self.tipo = tipo
        self.ganador = False
    
    
    def realizarJugadaM(self):
        from clases.juego import Juego

        posibleJugada = self.buscarCoincidencia(self.mazo)
        dobles = self.buscarDobles(set(posibleJugada[0]+posibleJugada[-1]))
        
        if len(dobles) == 2:
            doble = Jugada("PONER", dobles)
            print(dobles,Juego.RegistroJugadas[0][0])
            if dobles[0][0]==Juego.RegistroJugadas[0][0]:
                pos1,pos2 = 0,-1
            else:
                pos1,pos2 = -1,0
            
            doble.colocarDoble(self.mazo, pos1,pos2)
            return f"{self.tipo} ha puesto la pieza {dobles[0]} y la pieza {dobles[1]}"
        

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

        if accion != 0 and accion != 1: return "jugada invalida"

        if accion == 1:
            Jugada("PASAR",None)
            return "paso"
        
        if indexPieza>=len(self.mazo.piezas): return "jugada invalida"

        if pos !=0 and pos!=1: return "jugada invalida"

        piezaEnMazo = self.mazo.piezas[indexPieza]
        jugada,pieza,tipo = Jugada.probarJugada(piezaEnMazo,pos)
        
        if not jugada: return "jugada invalida"
        
        J = Jugada("PONER",pieza)
        J.colocarPieza(self.mazo,tipo) 
        return f"{self.tipo} ha puesto la pieza {pieza}"  

    def realizarJugadaHAux(self,accion,indexPieza,pos):

        if accion != 0 and accion != 1: return "jugada invalida"

        if accion == 1:
            Jugada("PASAR",None)
            return "paso"
        
        piezas = []
        tipos = []
        for i in range(2):

            if indexPieza[i]>=len(self.mazo.piezas): return "jugada invalida"

            if pos[i] !=0 and pos[i]!=1: return "jugada invalida"

            piezaEnMazo = self.mazo.piezas[indexPieza[i]]
            jugada,pieza,tipo = Jugada.probarJugada(piezaEnMazo,pos[i])
            
            if not jugada: return "jugada invalida"
            
            piezas.append(pieza)
            tipos.append(tipo)
        
        J = Jugada("PONER",piezas)
        J.colocarDoble(self.mazo,tipos[0],tipos[1])
        return f"{self.tipo} ha puesto la pieza {piezas[0]} y la pieza {piezas[1]}"
        

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

    def buscarDobles(self,lista):
        doble = []
        for i in list(lista):
            if i[0]==i[-1]:
                doble += [i]
        return doble


    def __str__(self):
        return f"{self.tipo} {self.mazo}"
