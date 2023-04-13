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
            entrada, piezas, pos, desicion = int(input()), [],[], None
            
            if entrada == 0:
                bucle = 1
                
                if jugador.mazo.piezadoble > 1:
                    desicion = input("tiene mas de 2 fichas dobles, desea realizar una jugada doble? y/n\n")
                    
                    if desicion == "y":
                        bucle = 2

                for _ in range(bucle):
                    piezas += [int(input(f"numero de la posicion de la pieza(del 1 al {len(jugador.mazo.piezas)})\n"))-1]
                    pos += [int(input("Donde vas a poner la pieza? : 0 para inicio, 1 para final\n"))]
            
            

            if desicion == "y":
                print(jugador.realizarJugadaHAux(entrada, piezas, pos))
            elif entrada == 0:
                print(jugador.realizarJugadaH(entrada, piezas[0], pos[0]))
            else:
                print(jugador.realizarJugadaH(entrada, None, None))

        print(Juego.RegistroJugadas)
        self.juego.finalizar()

        if Juego.EstadoJuego == False:
            print(self.juego)



    def __str__(self):
        return f"{self.juego}"
        
        
        
    

#se debe llamar a main con X humanos
Main(1)
