class Jugada():
    turno = 0
    turnosPaso = 0
    def __init__(self, accion, pieza):
        self.accion = accion
        self.pieza = pieza
        Jugada.turno += 1
        
        #reinicia el contador de jugada para que asi el juego sea rotativo
        if Jugada.turno >3:
            Jugada.turno = 0
        
        #guarda los turnos que ha pasado para asi tener un 
        #numero con el cual saber cuando no hay mas jugadas dsiponibles
        if accion == "PASAR":
            Jugada.turnosPaso +=1
        else:
            Jugada.turnosPaso = 0
     
           
    #funcion nucleo que coloca la pieza en el tablero y actualiza las variables del mazo
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


    #funcion auxiliar que ayuda a colocar correctamente 2 piezas a la vez
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


    #comprobar si los parametros de la pieza entragada  
    # por el jugador es valido
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

        return False,None,None


    #a partir del parametro con el que se inicio el mazo se asigna el turno inicial del cual el juego va a partir
    @classmethod
    def asignarTurnoInicial(src,jugadores):
        from clases.juego import Juego
        
        j = 0
        for i in jugadores:
            
            if i.mazo.inicia == True:

                Jugada.turno = j
                J = Jugada("PONER","6:6")
                Juego.RegistroJugadas += [J.pieza]

                #estructura utilizada para remover una pieza del mazo
                i.mazo.piezas.remove("6:6")
                i.mazo.piezasInv.remove("6:6")
                i.mazo.piezadoble -= 1
                break
            
            j += 1
        

    def __str__(self):
        
        if self.accion == "PONER":
            return f"Turno del jugador {self.turno}. accion = {self.accion}, donde puso {self.pieza}."
        else:
            return f"El jugador {self.turno} ha pasado el turno."