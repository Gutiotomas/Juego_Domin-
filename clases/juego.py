from clases.mazo import Mazo
from clases.jugador import Jugador
class Juego():
    def __init__(self, EstadoJuego, humanos,RegistroJugadas = list()):

        self.EstadoJuego = EstadoJuego #para verificar si alguien ya ganó
        self.RegistroJugadas = RegistroJugadas #para imprimir por pantalla las fichas
        self.mazos = self.inicializarMazos()
        self.jugadores = self.inicializarjugadores(humanos)
        self.RegistroJugadas = RegistroJugadas


    def inicializarMazos(self):
        ListaPiezas = [f"{a}:{b}" for a in range(0,7) for b in range(a,7)]
        Mazos = []
        for _ in range(4):
            Mazos += [Mazo(ListaPiezas,7)]
        return Mazos

    def inicializarjugadores(self,numero):
        players = []
        for i in range(numero):
            players += [Jugador(f"HUMANO {i+1}", self.mazos[i])] 
        machines = []
        for i in range(numero,4):
            machines += [Jugador(f"MAQUINA {i -numero +1}", self.mazos[i])]
        return players + machines



    def finalizar():
        pass

    def mostrarJugada():
        pass

    def __str__(self):
        return f"{self.jugadores[0]},\n\
{self.jugadores[1]},\n\
{self.jugadores[2]},\n\
{self.jugadores[3]}"