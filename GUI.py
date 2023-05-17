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

coords=[]
def colocarPieza(nombre, ubicacion, orientacion):

    global coords
    x,y,c,d = 0,0,0,0

    if nombre == "6:6":
        coordsI = (pantalla.get_rect().centerx - 12, pantalla.get_rect().centery)
        coordsD = (pantalla.get_rect().centerx + 11, pantalla.get_rect().centery)
        ficha = Ficha(nombre[0], coordsD,orientacion)
        ficha2 = Ficha(nombre[-1], coordsI,orientacion)
        coords = [coordsI,coordsD]
        return TodosSprites.add(ficha,ficha2)

    elif orientacion == 0:
        x,y,c,d = 24, 0, -1, 0

    elif orientacion == 1:
        x,y,c,d = 0,-24, 0, 1

    elif orientacion == 2:
        x,y,c,d = -24, 0, 1, 0

    else:
        x,y,c,d = 0, 24, 0, -1

    if ubicacion == 0:
        Coords = coords[0]
        coords[0] = Coords[0] + 2*x+c , Coords[1] + 2*y+d
    else: 
        Coords = coords[1]
        coords[1] = Coords[0] + 2*x+c , Coords[1] + 2*y+d
    
    if ubicacion == 0:
        nombre = nombre[::-1]

    ficha = Ficha(nombre[0], (Coords[0] + x, Coords[1] + y) ,orientacion)
    ficha2 = Ficha(nombre[-1], (Coords[0] + 2*x+c , Coords[1] + 2*y+d), orientacion)
    TodosSprites.add(ficha,ficha2)
    return (Coords[0] + 2*x+c , Coords[1] + 2*y+d)
            
def comprobarPosicion(anteriorOrientacion):
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
n1 = 0
print(colocarPieza("6:6",0,n1))
n1 = random.choice(comprobarPosicion(n1))

juego = Main()
print(Juego.RegistroJugadas)

keys = [pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7]
while True:
    clock = pygame.time.Clock()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if Juego.EstadoJuego:
        jugador = juego.juego.jugadores[Jugada.turno]
        if jugador.tipo[0]=="M": #ejecutar la "IA"
            maquina = jugador.realizarJugadaM()
            print(maquina)
            if maquina[1] != None:
                for i in range(len(maquina[1])):
                    colocarPieza(maquina[1][i],maquina[2][i],n1)
                n1 = random.choice(comprobarPosicion(n1))
    juego.juego.finalizar()

    
        
    
    
    TodosSprites.draw(pantalla)
    pygame.display.flip()
    clock.tick(60)



