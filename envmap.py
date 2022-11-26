#Obtiene colores de pixel de bmp

#Imports de struct, color y vectores
import struct
from vector import *
from coloration import *
from math import *

class EP:
    def __init__(self, path):
        self.path = path
        self.read()

    def transformation(self, direction):
        self.actual = direction
        # print(self.actual)
        x = (atan2(self.actual.z, self.actual.x)/(2*pi)+(1/2))*self.width
        y = (-acos(self.actual.y)/pi)*self.height
        # print(self.pixels[y][x])
        return self.pixels[round(y)][round(x)]

    def read (self):
        with open (self.path, "rb") as image:

            image.seek(2 + 4 + 2 + 2)
            header_size = struct.unpack("=l", image.read(4))[0]

            image.seek(2+4+2+2+4+4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)
            self.pixels = []

            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(color(r,g,b))
