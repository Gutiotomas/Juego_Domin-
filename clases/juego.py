from clases.mazo import Mazo
from clases.jugador import Jugador
from clases.jugada import Jugada
class Juego():
    EstadoJuego = True #para verificar si alguien ya ganó
    RegistroJugadas = list() #para imprimir por pantalla las fichas
    def __init__(self, humanos):

        self.mazos = self.inicializarMazos()
        self.jugadores = self.inicializarjugadores(humanos)
        Jugada.asignarTurnoInicial(self.jugadores)
        


    def inicializarMazos(self):
        ListaPiezas = [f"{a}:{b}" for a in range(0,7) for b in range(a,7)]
        Mazos = []
        for _ in range(4):
            Mazos += [Mazo(ListaPiezas,7)]
        return Mazos

    def inicializarjugadores(self,numero):
        players = []
        for i in range(numero):
            p = Jugador(f"HUMANO {i+1}", self.mazos[i])
            self.mazos[i].jugador = p
            players += [p]                 
        machines = []
        for i in range(numero,4):
            m = Jugador(f"MAQUINA {i -numero +1}", self.mazos[i])
            self.mazos[i].jugador = m
            machines += [m]
        return players + machines



    @classmethod
    def finalizar(cls,juego):
        for i in juego.jugadores:
            if len(i.mazo.piezas) == 0:
                Juego.EstadoJuego =False
                i.ganador = True
        if Jugada.turnosPaso > 5:
            Juego.EstadoJuego =False
    
    def ganador(self):
        #definir el ganador cuando no hay mas jugadas
        pass



    def __str__(self):
        return f"{self.jugadores[0]}\n\
{self.jugadores[1]}\n\
{self.jugadores[2]}\n\
{self.jugadores[3]}"