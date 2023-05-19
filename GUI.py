import pygame, sys, random
from clases.juego import Juego
from clases.jugada import Jugada
from main import Main


def reaccionar():
    pass


class Ficha(pygame.sprite.Sprite):
    def __init__(self,numero,Coords,orientacion):
        super().__init__()
        if orientacion%2==1:
            self.image = pygame.image.load(f"assets/Piezas/{numero}.png").convert()
        else:
            self.image = pygame.image.load(f"assets/Piezas/{numero}_rotado.png").convert()
        
        self.rect = self.image.get_rect()
        self.rect.center = Coords


class Boton(pygame.sprite.Sprite):
    def __init__(self, Coords):
        super().__init__()
        self.rect = self.image.get_rect()
        self.rect.center = Coords



def iniciarMazo(mazo):

    for i in range(len(mazo)):
        ficha = Ficha(mazo[i][0],(pantalla.get_rect().centerx -((24+2)*3+6)+((24+2)*i),650),3)   
        ficha2 = Ficha(mazo[i][-1],(pantalla.get_rect().centerx -((24+2)*3+6)+((24+2)*i),650 + 23),3)      
        
        listaFicha.add(ficha,ficha2)
        TodosSprites.add(ficha,ficha2)

aux = set()
def verificarColision(imagen_sprite1, grupo_sprites2,ubicacion):
    aux.add(ubicacion)
    if len(aux)<2:
        return False
    colision_sprites = pygame.sprite.spritecollide(imagen_sprite1, grupo_sprites2, False)
    return bool(colision_sprites)


coords=[]
def Coordenadas(orientacion):
    global coords
    x,y,c,d = 0,0,0,0

    if orientacion == 0:
        x,y,c,d = 24, 0, -1, 0

    elif orientacion == 1:
        x,y,c,d = 0, -24, 0, 1

    elif orientacion == 2:
        x,y,c,d = -24, 0, 1, 0

    else:
        x,y,c,d = 0, 24, 0, -1
        
    return (x, y),(2*x+c , 2*y+d)
    


def colocarPieza(nombre, ubicacion, orientacion):

    global coords
    global cabezaCola
    if nombre == "6:6":
        coords1 = (pantalla.get_rect().centerx - 12, pantalla.get_rect().centery) 
        coords0 = (pantalla.get_rect().centerx + 11, pantalla.get_rect().centery)
        ficha = Ficha(nombre[0], coords1,orientacion)
        ficha2 = Ficha(nombre[-1], coords0,orientacion)
        coords = [coords0,coords1]
        return TodosSprites.add(ficha,ficha2)
    


    if ubicacion == 1:
        nombre = nombre[::-1]
    x, y = coords[ubicacion][0], coords[ubicacion][1]
    Coords = Coordenadas(orientacion)
    ficha = Ficha(nombre[0], (x + Coords[0][0], y + Coords[0][1]), orientacion)
    ficha2 = Ficha(nombre[-1], (x + Coords[1][0], y + Coords[1][1]), orientacion)
    NewCoordenadas = cabezaCola[ubicacion]
    contador = 0
    while verificarColision(ficha2,TodosSprites,ubicacion):
        if contador == 10:
            break
        NewCoordenadas = random.choice(comprobarOrientacion(NewCoordenadas))
        Coords = Coordenadas(NewCoordenadas)
        
        ficha = Ficha(nombre[0], (x + Coords[0][0], y + Coords[0][1]), NewCoordenadas)
        ficha2 = Ficha(nombre[-1], (x + Coords[1][0], y + Coords[1][1]), NewCoordenadas)


    coords[ubicacion] = (x + Coords[1][0], y + Coords[1][1])
    cabezaCola[ubicacion] = NewCoordenadas 

    TodosSprites.add(ficha,ficha2)

    return coords, coords[ubicacion], Coords[1]


def comprobarOrientacion(anteriorOrientacion):
    orientaciones = [0,1,2,3]
    mapping = {0: 2, 1: 3, 2: 0, 3: 1}
    orientaciones.pop(mapping[anteriorOrientacion])
    return orientaciones



#pantalla
pygame.init()
pantalla = pygame.display.set_mode((1200,800))

#titulos
pygame.display.set_caption("Domino")
icono = pygame.image.load("assets/icon.png")

#fondo
fondo = pygame.image.load("assets/background.jpg").convert()
pygame.display.set_icon(icono)
pantalla.blit(fondo,(0,0))

#guardar los sprites
listaFicha = pygame.sprite.Group()
TodosSprites = pygame.sprite.Group()

#iniciar los sprites
mazo = ['5:6', '0:4', '2:5', '3:6', '5:5', '3:5', '2:2']
iniciarMazo(mazo)
colocarPieza("6:6",0,0) 
cabezaCola = [random.choice(comprobarOrientacion(0)),random.choice(comprobarOrientacion(2))]
juego = Juego(0)
Juego.RegistroJugadas

keys = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7]
while True:
    
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if Juego.EstadoJuego:
        jugador = juego.jugadores[Jugada.turno]

        if jugador.tipo[0]=="M": #ejecutar la "IA"

            maquina = jugador.realizarJugadaM()
            #maquina = [None,None,None]

            if maquina[1] != None:

                for i in range(len(maquina[1])):

                    colocarPieza(maquina[1][i],maquina[2][i],cabezaCola[maquina[2][i]])
                    cabezaCola[maquina[2][i]] = random.choice(comprobarOrientacion(cabezaCola[maquina[2][i]]))
    
    juego.finalizar()

    TodosSprites.draw(pantalla)
    pygame.display.flip()
    clock.tick(60)



