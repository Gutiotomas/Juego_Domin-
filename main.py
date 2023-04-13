from clases.juego import Juego
from clases.jugada import Jugada

class Main():

    def __init__(self,humanos):
        #inicializa el juego junto con los jugadores y maquinas
        self.juego = Juego(humanos)
        
        #bucle principal del juego
        print(Juego.RegistroJugadas)
        while Juego.EstadoJuego:
            self.jugar()
        
        #discriminar al ganador
        for i in self.juego.jugadores:
            if i.ganador:
                print(f"{i.tipo} es el ganador.")


    #funcion que ejecuta las entradas y salidas del juego     
    def jugar(self):
        
        jugador = self.juego.jugadores[Jugada.turno]
        
        if jugador.tipo[0]=="M": #ejecutar la "IA"
            print(jugador.realizarJugadaM())
        
        else: #se ve largo por la cantidad de entradas que tiene el codigo pero es facil de entender
            #mostrar por pantalla las opciones
            print(jugador.mazo)
            print("=Opciones: Poner ficha = 0, Pasar turno = 1.")
            entrada, piezas, pos, desicion = int(input()), [],[], None
            
            if entrada == 0:
                bucle = 1
                #filtrar si hay posibilidad de una jugada doble
                if jugador.mazo.piezadoble > 1:
                    desicion = input("Tiene más de 2 fichas dobles, ¿desea realizar una jugada doble? y/n.\n")
                    
                    if desicion == "y":
                        bucle = 2

                for _ in range(bucle):
                    piezas += [int(input(f"Número de la posicion de la pieza(del 1 al {len(jugador.mazo.piezas)}).\n"))-1]
                    pos += [int(input("¿Dónde vas a poner la pieza? 0 para inicio, 1 para final.\n"))]
            
            #llamado a las funciones que es encargan de veriicar que las entradas funcionen
            if desicion == "y":
                print(jugador.realizarJugadaHAux(entrada, piezas, pos))
            elif entrada == 0:
                print(jugador.realizarJugadaH(entrada, piezas[0], pos[0]))
            else:
                print(jugador.realizarJugadaH(entrada, None, None))

        #imprimir el tablero y varificar el estado del mismo
        print(Juego.RegistroJugadas)
        self.juego.finalizar()

        if Juego.EstadoJuego == False:
            print(self.juego)


    def __str__(self):
        return f"{self.juego}"
        
        
        
    

#se debe llamar a main con X humanos
Main(1)
