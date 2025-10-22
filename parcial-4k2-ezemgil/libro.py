from material import Material

class Libro(Material):
    def __init__(self, codigo, titulo, autor, precio_base, dias_prestados):
        super().__init__(codigo, titulo, autor, precio_base, tipo=1)
        self.dias_prestados = int(dias_prestados)
        self.dias_en_biblioteca = int(dias_prestados)

    def calcular_costo_mantenimiento(self):
        if self.dias_prestados < 30:
            return 100
        return ((self.dias_prestados // 30) + 1) * 100

    def __str__(self):
        return f"Libro: {self.codigo} - {self.titulo} - Autor: {self.autor} - Precio Base: {self.precio_base} - Días Prestados: {self.dias_prestados}"