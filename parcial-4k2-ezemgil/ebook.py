from material import Material

class Ebook(Material):
    def __init__(self, codigo, titulo, autor, precio_base, valor_venta):
        super().__init__(codigo, titulo, autor, precio_base, tipo=2)
        self.valor_venta = int(valor_venta)

    def calcular_costo_mantenimiento(self):
        return self.valor_venta * 0.05
    
    def __str__(self):
        return f"Ebook: {self.codigo} - {self.titulo} - Autor: {self.autor} - Precio Base: {self.precio_base} - Valor Venta: {self.valor_venta}"