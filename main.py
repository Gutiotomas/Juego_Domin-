from clases.juego import Juego
from clases.jugada import Jugada

class Main():

    def __init__(self,humanos=0):
        #inicializa el juego junto con los jugadores y maquinas
        self.juego = Juego(humanos)
        self.Inicio()
        #bucle principal del juego
        print(self.juego.jugadores[(Jugada.turno-1)%4].tipo,"ha puesto la pieza 6:6",Juego.obtenerPiezaUnicode("6:6",1))
        print(Juego.RegistroUnicode)
        print(Juego.ImprimirBonito())
        print()

        while Juego.EstadoJuego:
            self.jugar()
        
        #discriminar al ganador
        for i in self.juego.jugadores:
            if i.ganador:
                print(f"\n\n{i.tipo} es el ganador.\n\n")


    #funcion que ejecuta las entradas y salidas del juego     
    def jugar(self):
        
        jugador = self.juego.jugadores[Jugada.turno]
        
        if jugador.tipo[0]=="M": #ejecutar la "IA"
            print(jugador.realizarJugadaM()[0])
        
        else: #se ve largo por la cantidad de entradas que tiene el codigo pero es facil de entender
            #mostrar por pantalla las opciones
            print(jugador.mazo)
            print("Opciones: Pasar turno = 0, Poner ficha = 1, Jugada doble = 2")
            entrada, piezas, pos = input(), [],[]
            
            if entrada.isdigit():
                entrada = int(entrada)
            else:
                print("Opcion invalida.")
                return print(Juego.RegistroUnicode),print(Juego.ImprimirBonito())
            
            if entrada <0 or entrada > 2: 
                print("Opcion invalida.")
                return print(Juego.RegistroUnicode),print(Juego.ImprimirBonito())

            for _ in range(entrada):
                
                pieza = input(f"Número de la posicion de la pieza(del 1 al {len(jugador.mazo.piezas)}).\n")
                posicion = input("¿Dónde vas a poner la pieza? Inicio = 0, Final = 1\n")
                
                if not (pieza.isdigit() and posicion.isdigit()):
                    print("Opcion invalida.")
                    return print(Juego.RegistroUnicode),print(Juego.ImprimirBonito())
                
                piezas += [int(pieza)-1]
                pos += [int(posicion)]
                
            #llamado a las funciones que es encargan de veriicar que las entradas funcionen
            if entrada == 2:
                print(jugador.realizarJugadaHAux(entrada, piezas, pos))
            elif entrada == 1:
                print(jugador.realizarJugadaH(entrada, piezas[0], pos[0]))
            else:
                print(jugador.realizarJugadaH(entrada, None, None))

        #imprimir el tablero y varificar el estado del mismo
        print(Juego.RegistroUnicode)
        print(Juego.ImprimirBonito())
        print()
        self.juego.finalizar()

        if Juego.EstadoJuego == False:
            print(self.juego)

    def Inicio(self):
        print("\n───────────────────────────────────────────────────\n\
             Bienvenido al juego Dominó\n\
            \n\
            Recuerda usar un complilador\n\
                con capacidad unicode\n\
            \n\
            Presiona 'Enter' para continuar\n\
──────────────────────────────────────────────────")
        return input()

    def __str__(self):
        return f"{self.juego}"
        

#se debe llamar a main con X humanos
Main(0)
