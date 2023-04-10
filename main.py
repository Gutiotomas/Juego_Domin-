from clases.juego import Juego
class Main():
    def __init__(self,humanos):
        self.juego = Juego(True, humanos)
    
    def __str__(self):
        return f"{self.juego}"
        
        
        
    

#se debe llamar a main con X humanos
print(Main(1))
