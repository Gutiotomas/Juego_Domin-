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

    def probarJugada():
        #comprobar si los parametros entregados por el jugador son validos
        pass


    def __str__(self):
        if self.accion == "PONER":
            return f"turno del jugador {self.turno}. accion = {self.accion}, donde puso {self.pieza}"
        else:
            return f"el jugador {self.turno} ha pasado el turno"