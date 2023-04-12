from clases.juego import Juego
from clases.jugada import Jugada

class Main():
    def __init__(self,humanos):
        self.juego = Juego(humanos)
        #bucle de juego(?)

        print(Juego.RegistroJugadas)
        while Juego.EstadoJuego:
            self.jugar()
            
    def jugar(self):
        jugador = self.juego.jugadores[Jugada.turno]
        if jugador.tipo[0]=="M":
            print("MAQUINA")
            print(jugador.realizarJugadaM())
        else:
            print("HUMANO")
            print(jugador.mazo)
            print("opciones:\nponer = 0\npasar = 1")
            entrada,pieza = int(input("accion: ")), None
            if entrada == 0:
                pieza = int(input("numero de la posicion de la pieza: "))
            print(jugador.realizarJugadaH(entrada, pieza))

        print(Juego.RegistroJugadas)
        Juego.finalizar(self.juego)
        if Juego.EstadoJuego == False:
            self.juego



    def __str__(self):
        return f"{self.juego}"
        
        
        
    

#se debe llamar a main con X humanos
print(Main(1))
