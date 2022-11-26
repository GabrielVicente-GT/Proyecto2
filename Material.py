#Clase de material con albedo, defuse y espectro

class material:
    def __init__(self,defuse, albedo, spec, indice_refraccion = 0):
        self.refractive_index = indice_refraccion
        self.albedo = albedo
        self.defuse = defuse
        self.spec = spec