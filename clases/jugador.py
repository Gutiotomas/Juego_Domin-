from random import random,randint
from clases.jugada import Jugada

class Jugador():
    
    def __init__(self, tipo,mazo):
        self.mazo = mazo
        self.tipo = tipo
        self.ganador = False
    

    #realiza la jugada de la "IA" acpasa mediante el parametro tipo de cada jugador
    def realizarJugadaM(self):
        from clases.juego import Juego

        posibleJugada = self.buscarCoincidencia(self.mazo)
        dobles = self.buscarDobles(set(posibleJugada[0]+posibleJugada[-1]))
        #si encuentra 2 dobles si o si pone las dos fichas
        if len(dobles) == 2:
            doble = Jugada("PONER", dobles)
            print(dobles,Juego.RegistroJugadas[0][0])
            if dobles[0][0]==Juego.RegistroJugadas[0][0]:
                pos1,pos2 = 0,-1
            else:
                pos1,pos2 = -1,0
            
            doble.colocarDoble(self.mazo, pos1,pos2)
            return f"{self.tipo} ha puesto la pieza {dobles[0]} y la pieza {dobles[1]}."
        
        #en caso de que no tenga fichas para jugar
        if posibleJugada == ([],[]):
            Jugada("PASAR",None)
            return f"{self.tipo} pasa el turno."

        #genera un 50% de probabilidades de elegir un lado o el otro, en caso de que el lado elegido no tenga items pasa
        if random()<=0.5 and posibleJugada[0]!= []: 
            cabeza =  posibleJugada[0][randint(0,len(posibleJugada[0])-1)]
            maquina = Jugada("PONER",cabeza)
            maquina.colocarPieza(self.mazo,0)
            return f"{self.tipo} ha puesto la pieza {cabeza}."
        
        elif posibleJugada[-1]!= []:
            cola =  posibleJugada[-1][randint(0,len(posibleJugada[-1])-1)]
            maquina = Jugada("PONER",cola)
            maquina.colocarPieza(self.mazo,-1)
            return f"{self.tipo} ha puesto la pieza {cola}."
        
        else:
            Jugada("PASAR",None)
            return f"{self.tipo} pasa el turno."
    

    #realiza la jugada del jugador acpasa mediante el parametro tipo de cada jugador
    #tiene un monton de casos de exepcion
    def realizarJugadaH(self,accion,indexPieza,pos):

        if accion == 0:
            Jugada("PASAR",None)
            return f"{self.tipo} pasa el turno."
        
        if indexPieza>=len(self.mazo.piezas): return "Jugada inválida."

        if pos !=0 and pos!=1: return "Jugada inválida."

        #busca si la ficha si es valida para jugarla
        piezaEnMazo = self.mazo.piezas[indexPieza]
        jugada,pieza,tipo = Jugada.probarJugada(piezaEnMazo,pos)
        
        if not jugada: return "Jugada inválida."
        
        #juega la ficha en caso de que sea valida la jugada y haya pasado todos los filtros anteriores
        J = Jugada("PONER",pieza)
        J.colocarPieza(self.mazo,tipo) 
        return f"{self.tipo} ha puesto la pieza {pieza}."  


    #funcion auxiliar para realizar 2 jugadas
    def realizarJugadaHAux(self,accion,indexPieza,pos):

        if accion == 0:
            Jugada("PASAR",None)
            return f"{self.tipo} pasa el turno."
        #almacenar las 2 posiciones de las fichas y las fichas
        piezas = []
        tipos = []
        for i in range(2):

            if indexPieza[i]>=len(self.mazo.piezas): return "Jugada inválida."

            if pos[i] !=0 and pos[i]!=1: return "Jugada inválida."

            #busca si la ficha si es valida para jugarla
            piezaEnMazo = self.mazo.piezas[indexPieza[i]]
            jugada,pieza,tipo = Jugada.probarJugada(piezaEnMazo,pos[i])
            
            if not jugada: return "Jugada inválida."
            
            piezas.append(pieza)
            tipos.append(tipo)

        #juega las fichas en caso de que sea valida la jugada y haya pasado todos los filtros anteriores
        J = Jugada("PONER",piezas)
        J.colocarDoble(self.mazo,tipos[0],tipos[1])
        return f"{self.tipo} ha puesto la pieza {piezas[0]} y la pieza {piezas[1]}."


    #funcion que hace que la "IA" busque todas las opciones de posibles jugadas
    def buscarCoincidencia(self,mazo):
        from clases.juego import Juego

        NewCabeza = []
        NewCola = []
        primera, ultima = Juego.RegistroJugadas[0][0],Juego.RegistroJugadas[-1][-1]
        
        #saca todos los items que sean una posibilidad para realizar la jugada
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


    #funcion auxiliar que ayuda a la "IA" a biscar todas las fichas repetidas en su mazo
    def buscarDobles(self,lista):
        doble = []
        for i in list(lista):
            if i[0]==i[-1]:
                doble += [i]
        return doble


    def __str__(self):
        return f"{self.tipo} {self.mazo}"
