
#Raytracer
from Render import *
from fiRender import *
from math import *
from vector import *
from Sphere import *
from flat import *
from Material import *
from intersection import *
from light import *
from coloration import *

from envmap import *
max_recursion_depth = 3

class Raytracer(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.background_color = color(100,0,0)
        self.current_color = color(255,255,255)
        self.objetos = []
        self.luz = None

        self.clear_2(EP('./Fondo.bmp'))


    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range (self.width)]
            for y in range(self.height)
        ]

    def clear_2(self, valor):
        self.back_color_renoved = valor
        self.framebuffer = [
            [valor.pixels[y][x] for x in range (self.width)]
            for y in range(self.height)
        ]
        # for x in range (len(self.framebuffer)):
        #     for y in range (len(self.framebuffer[x])):
        #         print(self.framebuffer[x][y])

    def point(self, x,y, c = None):
        if y >= 0 and y < self.height and x >= 0 and x < self.width:
            self.framebuffer[y][x] = c or self.current_color

    def write(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)

    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)

        for y in range(self.height):
            for x in range(self.width):
                i = ((2*(x+0.5)/self.width)-1)* ar * tana
                j = (1-(2*(y+0.5)/self.height)) * tana

                direction = V3(i,j,-1).normalize()
                origin = V3(0,0,0)
                c = self.cast_ray(origin, direction)

                self.point(x,y,c)

    def cast_ray(self,origin,direction, recursion = 0):

        if recursion >= max_recursion_depth:
            try:
                return self.back_color_renoved.transformation(direction)
            except:
                return self.background_color


        material, intersect = self.scene_intersect(origin,direction)

        if material is None:
            try:
                return self.back_color_renoved.transformation(direction)
            except:
                return self.background_color
        light_dir = (self.luz.position - intersect.point).normalize()



        #Sombra
        blast_sombra = 1.1
        origen_sombra = intersect.point +(intersect.normal * blast_sombra)
        material_sombra, material_int = self.scene_intersect(origen_sombra, light_dir)
        intensidad_sombra = 0
        if material_sombra:
            intensidad_sombra = 0.3


        #Diffuse componente

        intesnity = light_dir @ intersect.normal

        # defuse = color(
        #     int(material.defuse[2] * intesnity),
        #     int(material.defuse[1] * intesnity),
        #     int(material.defuse[0] * intesnity)
        # )
        defuso_interno = material.defuse * intesnity * material.albedo[0] * (1-intensidad_sombra)

        #Specular componente
        light_refleccion = reflect(light_dir,intersect.normal)
        reflejo_i =max(0, (light_refleccion @ direction))
        specular_i = reflejo_i**material.spec
        specular = self.luz.c * specular_i * material.albedo[1]

        #reflection
        if material.albedo[2] > 0:
            reverse_direction = direction *1
            refleccion_direcion = reflect(reverse_direction, intersect.normal)
            refleccion_blass = -0.5 if refleccion_direcion @ intersect.normal < 0 else 0.5
            refleccion_origen = intersect.point + (intersect.normal * refleccion_blass)
            refleccion_color = self.cast_ray(refleccion_origen, refleccion_direcion,  recursion+1)
        else:
            refleccion_color = color(0,0,0)

        refleccion = refleccion_color * material.albedo[2]

        #refrrax
        if material.albedo[3] > 0:
            refrax_direcion = refract(direction, intersect.normal, material.refractive_index)
            refrax_blass = -0.5 if refrax_direcion @ intersect.normal < 0 else 0.5
            refrax_origen = intersect.point + (intersect.normal * refrax_blass)
            refrax_color = self.cast_ray(refrax_origen, refrax_direcion, recursion+1)
        else:
            refrax_color = color(0,0,0)

        refrax = refrax_color* material.albedo[3]

        return defuso_interno + specular + refleccion + refrax
        # for o in range(len(self.objetos)):
        #     material = self.scene_intersect(origin,direction)
        #     if material:
        #         return material.defuse

        # return self.background_color

        # for o in range(len(self.objetos)):
        #     if self.objetos[o].ray_intersect(origin, direction):
        #         return self.colores[o]

        # return self.background_color

    def scene_intersect(self, origin, direction):
        zbuffer = 999999
        material = None
        intersect = None

        for o in self.objetos:
            o_intersect = o.ray_intersect(origin,direction)
            if o_intersect:
                if o_intersect.distance < zbuffer:
                    # return o.material
                    zbuffer = o_intersect.distance
                    material = o.material
                    intersect = o_intersect

        return material, intersect

