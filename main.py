#Gabriel Alejandro Vicente Lorenzo
#20498

#Proyecto 2 20498

from RayTracer import *
from Material import *
from coloration import *
from Sphere import *
from flat import *
from conoide import *

#Materiales
naranjapalido   = material(defuse = color(176, 148, 86),    albedo = [0.6,0.3, 0.1,0], spec = 30)
oscuridad       = material(defuse = color(0,0,0),    albedo = [0.6,0.3, 0.1,0], spec = 30)
vesh            = material(defuse = color(212, 136, 102),   albedo = [0.9, 0.1, 0,0], spec = 50)
ivory           = material(defuse = color(200,200,180),     albedo = [0.6,0.3, 0.1,0],  spec = 50)
rubber          = material(defuse = color(180, 0, 0),       albedo = [0.9, 0.1, 0,0],   spec = 10)
gris_palido     = material(defuse = color(255,255,255),     albedo = [0.6,0.3, 0.1,0],  spec = 50)
espejo          = material(defuse = color(255,255,255 ),    albedo = [0,1,0.8,0],       spec = 1425)
vidrio          = material(defuse = color(150,180,200 ),    albedo = [0,0.5,0.1, 0.8],  spec = 1425,    indice_refraccion= 1.5)

#Tama;o del render
r                   = Raytracer(800,600)

#Luz mundial
r.luz = Light(V3(-8, 26, 19), 2, color(255, 255, 255))

#Objetos que conforman la escena
r.objetos = [

    # #Corazon estructura
    Esfera(V3(0.12, -1, -4), 0.10, vesh),
    #Izquierda
    Esfera(V3(0.12-0.10, -1.20, -4), 0.12, vesh),
    Esfera(V3(0.12-0.23, -1.40, -4), 0.13, vesh),
    Esfera(V3(0.12-0.40, -1.55, -4), 0.15, vesh),
    Esfera(V3(0.12-0.60, -1.65, -4), 0.17, vesh),
    Esfera(V3(0.12-0.8, -1.7, -4), 0.2, vesh),
    Esfera(V3(0.12-0.8-0.2, -1.65, -4), 0.17, vesh),
    Esfera(V3(0.12-0.8-0.40, -1.55, -4), 0.15, vesh),
    Esfera(V3(0.12-0.8-0.57, -1.40, -4), 0.13, vesh),
    Esfera(V3(0.12-0.8-0.66-0.05, -1.20, -4), 0.12, vesh),

    Esfera(V3(0.12-0.8-0.66-0.11, -1.05, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66-0.13, -0.90, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66-0.15, -0.75, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66-0.13, -0.60, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66-0.09, -0.45, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66-0.00, -0.30, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.10, -0.15, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.20, 0, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.30, +0.15, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.40, +0.30, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.50, +0.45, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.60, +0.60, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.70, +0.75, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.80, +0.90, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+0.90, +1.05, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+1.00, +1.20, -4), 0.12, vesh),
    Esfera(V3(0.12-0.8-0.66+1.10, +1.35, -4), 0.12, vesh),
    #Derecha
    Esfera(V3(0.12+0.10, -1.20, -4), 0.12, vesh),
    Esfera(V3(0.12+0.23, -1.40, -4), 0.13, vesh),
    Esfera(V3(0.12+0.40, -1.55, -4), 0.15, vesh),
    Esfera(V3(0.12+0.60, -1.65, -4), 0.17, vesh),
    Esfera(V3(0.12+0.8, -1.7, -4), 0.2, vesh),
    Esfera(V3(0.12+0.8+0.2, -1.65, -4), 0.17, vesh),
    Esfera(V3(0.12+0.8+0.40, -1.55, -4), 0.15, vesh),
    Esfera(V3(0.12+0.8+0.57, -1.40, -4), 0.13, vesh),
    Esfera(V3(0.12+0.8+0.66, -1.20, -4), 0.12, vesh),

    Esfera(V3(0.12+0.8+0.66+0.11, -1.05, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66+0.13, -0.90, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66+0.15, -0.75, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66+0.13, -0.60, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66+0.09, -0.45, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66+0.00, -0.30, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.10, -0.15, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.20, 0, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.30, +0.15, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.40, +0.30, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.50, +0.45, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.60, +0.60, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.70, +0.75, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.80, +0.90, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-0.90, +1.05, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-1.00, +1.20, -4), 0.12, vesh),
    Esfera(V3(0.12+0.8+0.66-1.10, +1.35, -4), 0.12, vesh),
    #Lago
    Plane(V3(0,-1.5,-10),15,15,vidrio),
    #Puente
    Plane(V3(0.72,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0.12,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0.24,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0.36,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0.48,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0.60,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(-0.12,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(-0.24,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(-0.36,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(-0.48,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(-0.60,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(-0.72,-1.4,-2.8),0.1,2,naranjapalido),
    Plane(V3(0.84,-1.4,-2.8),0.1,2,naranjapalido),


    Plane(V3(0+0.07,-0.7,-2),0.5,0.3,naranjapalido),
    Plane(V3(0+0.07,-0.8,-2.2),0.55,0.3,oscuridad),
    Plane(V3(0+0.07,-0.9,-2.4),0.8,0.3,naranjapalido),
    Plane(V3(0+0.07,-1,-2.6),0.85,0.3,oscuridad),
    #Montañas
    Cone(V3(-4.5,0.5,-5),V3(-4.5,-0.45,-5),V3(-2,0.6,-5.5),1,gris_palido),
    Cone(V3(-4.5,0.7,-6),V3(-4.5,0.1,-6),V3(1,0.65,-5.5),1,gris_palido),
    Cone(V3(3.3,0.3,-5),V3(-0.7,0.6,-5),V3(4.5,0.7,-6),3,gris_palido),
    Cone(V3(0.7,0.7,-6),V3(1.5,0.3,-5),V3(5,0.8,-6),3,gris_palido),
    Cone(V3(0.55,-0.17,-4.5),V3(-0.7,0.6,-5),V3(2,0.7,-6),3,gris_palido)
]

r.render()
r.write('Proyecto2_20498.bmp')
