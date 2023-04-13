from clases.juego import Juego
from clases.jugada import Jugada

class Main():

    def __init__(self,humanos):
        self.juego = Juego(humanos)
        #bucle de juego(?)

        print(Juego.RegistroJugadas)
        while Juego.EstadoJuego:
            self.jugar()
        for i in self.juego.jugadores:
            if i.ganador:
                print(f"{i.tipo} es el ganador")
            
    def jugar(self):
        
        jugador = self.juego.jugadores[Jugada.turno]
        
        if jugador.tipo[0]=="M":
            print(jugador.realizarJugadaM())
        
        else:
            print(jugador.mazo)
            print("opciones: poner = 0 pasar = 1")
            entrada, pieza, pos = int(input()), None,None
            if entrada == 0:
                pieza = int(input(f"numero de la posicion de la pieza(del 1 al {len(jugador.mazo.piezas)})\n"))-1
                pos = int(input("Donde vas a poner la pieza? : 0 para inicio, 1 para final\n"))
            print(jugador.realizarJugadaH(entrada, pieza, pos))

        print(Juego.RegistroJugadas)
        self.juego.finalizar()

        if Juego.EstadoJuego == False:
            print(self.juego)



    def __str__(self):
        return f"{self.juego}"
        
        
        
    

#se debe llamar a main con X humanos
Main(1)
