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
        

    #genera una lista de las 28 fichas para jugar en el juego luego las reparte en 4 mazos
    # retorna los mazos de los jugadores
    def inicializarMazos(self):
        
        ListaPiezas = [f"{a}:{b}" for a in range(0,7) for b in range(a,7)]
        Mazos = []
        
        for _ in range(4):
            Mazos += [Mazo(ListaPiezas,7)]
        
        return Mazos


    #genera los 4 jugadores y dependiendo del parametro con el que se llamo al main pueden haber mas o menos "IA"s
    #a cada jugador le asinga un mazo
    # todos los jugadores son iguales entre si
    def inicializarjugadores(self,numero):
        
        players = []
        for i in range(numero):
            p = Jugador(f"HUMANO {i+1}", self.mazos[i])
            self.mazos[i].jugador = p
            players += [p]                 
        
        machines = []
        for i in range(numero,4):
            m = Jugador(f"MÁQUINA {i -numero +1}", self.mazos[i])
            self.mazos[i].jugador = m
            machines += [m]
        
        return players + machines



    #verifica el estado del juego y si alguien efectivamente ya gano
    def finalizar(self):
        
        for i in self.jugadores:
            if len(i.mazo.piezas) == 0:
                Juego.EstadoJuego =False
                i.ganador = True
        
        if Jugada.turnosPaso > 5:
            Juego.EstadoJuego =False
            self.ganador()


    #en caso de que se llegue a un punto sin fichas posibles para colocar dicernir por menor cantidad de "puntos"
    def ganador(self):
        resultado = []
        for jugador in self.jugadores:
            
            acum = 0
            for pieza in jugador.mazo.piezas:
                acum += int(pieza[0]) + int(pieza[-1])
            
            resultado.append(acum)
        
        Ganador = resultado.index(min(resultado))
        self.jugadores[Ganador].ganador = True


    def __str__(self):
        return f"{self.jugadores[0]}\n\
{self.jugadores[1]}\n\
{self.jugadores[2]}\n\
{self.jugadores[3]}"