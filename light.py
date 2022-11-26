#Clase de luz con posicion, intensidad y color
class Light:
    def __init__(self,position, intensity, c):
        self.c = c
        self.position = position
        self.intensity = intensity
