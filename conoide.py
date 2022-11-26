#Clase esfera que permite ddibujar una esfera
'''Referencia tomada de: https://www.scratchapixel.com/code.php?id=9&origin=/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle'''
from intersection import *
from vector import *

class Cone(object):
    def __init__(self, A, B, C, num,material):
        self.material = material
        self.num = num
        self.C = C
        self.A = A
        self.B = B

    def ray_intersect(self, origin, direction):

        primer_lado     = self.B - self.A
        segundo_lado    = self.C - self.A
        vectorial       = direction * segundo_lado
        determinante    = primer_lado @ vectorial

        if min(max(-1E-8, determinante),1E-8)==determinante:
            return None

        inverso_determinante    = 1 / determinante

        vectorial_cabezal       = origin - self.A
        multiplicacion_dot                    = vectorial_cabezal @ vectorial
        valor_u                 = inverso_determinante * multiplicacion_dot

        if min(max(valor_u,0),1) == 0 or min(max(valor_u,0),1) == 1:
            return None

        vectorial_cabezal_2       = vectorial_cabezal * primer_lado
        multiplicacion_dot = direction @ vectorial_cabezal_2
        valor_v = inverso_determinante * multiplicacion_dot

        if min(max(valor_v,0),1)==0 or min(max(valor_u+valor_v,0),1)==1:
            return None


        multiplicacion_dot = segundo_lado @ vectorial_cabezal_2
        resolution = inverso_determinante * multiplicacion_dot

        if max(resolution,0)==0:
            return None
        else:
            zona_impacto = origin +  direction * resolution
            if self.num == 1:
                vector_normalizado = (zona_impacto - self.A).normalize()
            elif self.num == 2:
                vector_normalizado = (zona_impacto - self.B).normalize()
            else:
                vector_normalizado = (zona_impacto - self.C).normalize()
            return Intersect(resolution, zona_impacto,vector_normalizado)