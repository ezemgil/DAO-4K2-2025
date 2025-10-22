from material import Material

class Revista(Material):
    def __init__(self, codigo, titulo, autor, precio_base, origen):
        super().__init__(codigo, titulo, autor, precio_base, tipo=3)
        self.origen = origen
        self.es_nacional = origen.lower() == 'nacional'

    def calcular_costo_mantenimiento(self):
        costo_base = 50
        if not self.es_nacional:
            costo_base *= 1.2 
        return costo_base

    def __str__(self):
        return f"Revista: {self.codigo} - {self.titulo} - Autor: {self.autor} - Precio Base: {self.precio_base} - Origen: {self.origen}"