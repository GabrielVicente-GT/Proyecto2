#Clase esfera que permite ddibujar una esfera

from intersection import *
from vector import *

class Plane(object):
    def __init__(self, center, w, l, material):
        self.material = material
        self.center = center
        self.l = l
        self.w = w

    def ray_intersect(self, origin, direction):
        d       = -(origin.y + self.center.y) / direction.y
        impact  = origin + (direction*d)
        normal  = V3(0,1,0)

        if  d <= 0 or impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) or impact.z > (self.center.z + self.l/2) or impact.z < (self.center.z - self.l/2):
            return None


        return Intersect(distance = d, point = impact, normal = normal)