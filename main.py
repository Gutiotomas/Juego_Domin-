from clases.juego import Juego
from clases.jugada import Jugada

class Main():
    def __init__(self,humanos):
        self.juego = Juego(humanos)

        #bucle de juego(?)

        print(Juego.RegistroJugadas)
        while Juego.EstadoJuego:
            self.jugar()
            print(Juego.RegistroJugadas)
            Juego.finalizar(self.juego)
            
            
    
    def jugar(self):
        jugador = self.juego.jugadores[Jugada.turno]
        if jugador.tipo[0]=="M":
            print("MAQUINA")
            print(jugador.realizarJugadaM())
        else:
            print("HUMANO")


    def __str__(self):
        return f"{self.juego}"
        
        
        
    

#se debe llamar a main con X humanos
print(Main(0))
