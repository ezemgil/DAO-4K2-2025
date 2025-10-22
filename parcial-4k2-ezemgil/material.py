from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, codigo, titulo, autor, precio_base, tipo):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio_base = int(precio_base)
        self.tipo = tipo

    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass

    def __str__(self):
        return f"{self.tipo}: {self.codigo} - {self.titulo} - Autor: {self.autor} - Precio Base: {self.precio_base}"