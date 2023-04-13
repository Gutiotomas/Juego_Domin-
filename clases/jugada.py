class Jugada():
    turno = 0
    turnosPaso = 0
    def __init__(self, accion, pieza):
        self.accion = accion
        self.pieza = pieza
        Jugada.turno += 1
        
        if Jugada.turno >3:
            Jugada.turno = 0
        
        if accion == "PASAR":
            Jugada.turnosPaso +=1
        else:
            Jugada.turnosPaso = 0
        
        

    @classmethod
    def asignarTurnoInicial(src,jugadores):
        from clases.juego import Juego
        
        j = 0
        for i in jugadores:

            if i.mazo.inicia == True:

                Jugada.turno = j
                J = Jugada("PONER","6:6")
                Juego.RegistroJugadas += [J.pieza]

                i.mazo.piezas.remove("6:6")
                i.mazo.piezasInv.remove("6:6")
                i.mazo.piezadoble -= 1
                break
            
            j += 1
        

    def colocarPieza(self, mazo, posicion):
        from clases.juego import Juego

        if posicion == 0:
            Juego.RegistroJugadas.insert(0,self.pieza)
        else:
            Juego.RegistroJugadas += [self.pieza]

        if self.pieza[0] > self.pieza[-1]: 
            self.pieza = self.pieza[::-1]
        
        if self.pieza[-1] == self.pieza[0]:
            mazo.piezadoble -= 1
        
        mazo.piezas.remove(self.pieza)
        mazo.piezasInv.remove(self.pieza[::-1])

    @classmethod
    def probarJugada(cls,pieza,pos):
        from clases.juego import Juego
        
        primera, ultima = Juego.RegistroJugadas[0][0],Juego.RegistroJugadas[-1][-1]
        if pos == 0:
            if pieza[-1] == primera:
                return True,pieza,0
            if pieza[0] == primera:
                return True,pieza[::-1],0
        else:
            if pieza[0] == ultima:
                return True,pieza,-1
            if pieza[-1] == ultima:
                return True,pieza[::-1],-1

        #comprobar si los parametros entregados 
        # por el jugador son validos

        return False,None,None
    
    def colocarDoble(self,mazo,pos1,pos2):
        from clases.juego import Juego
        
        if pos1 == 0:
            Juego.RegistroJugadas.insert(0,self.pieza[0])
            Juego.RegistroJugadas += [self.pieza[1]]
        else:
            Juego.RegistroJugadas.insert(0,self.pieza[1])
            Juego.RegistroJugadas += [self.pieza[0]]

        for i in self.pieza:
            if i[0] > i[-1]: 
                i = i[::-1]

            mazo.piezas.remove(i)
            mazo.piezasInv.remove(i[::-1])
            
        mazo.piezadoble -= 2
        
        


    def __str__(self):
        
        if self.accion == "PONER":
            return f"turno del jugador {self.turno}. accion = {self.accion}, donde puso {self.pieza}"
        else:
            return f"el jugador {self.turno} ha pasado el turno"