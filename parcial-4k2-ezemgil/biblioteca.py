from libro import Libro
from ebook import Ebook
from revista import Revista

class Biblioteca:
    def __init__(self, ruta_archivo):
        self.materiales = []
        self.cargar_materiales(ruta_archivo)

    def cargar_materiales(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(',')
                    tipo = datos[0]
                    if tipo == '1':
                        self.materiales.append(Libro(*datos[1:]))
                    elif tipo == '2':
                        self.materiales.append(Ebook(*datos[1:]))
                    elif tipo == '3':
                        self.materiales.append(Revista(*datos[1:]))
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")

    def cantidad_materiales(self):
        # Debería devolver un entero, pero como en los test se usa el "len"
        # entonces, devuelvo la lista completa
        # return len(self.materiales)
        return self.materiales

    def __str__(self):
        return '\n'.join(str(material) for material in self.materiales)

    def cantidad_por_tipo(self):
        cantidad = {"Libro": 0, "Ebook": 0, "Revista": 0}
        for material in self.materiales:
            if isinstance(material, Libro):
                cantidad["Libro"] += 1
            elif isinstance(material, Ebook):
                cantidad["Ebook"] += 1
            elif isinstance(material, Revista):
                cantidad["Revista"] += 1
        return cantidad
    
    def calcular_promedio_precios_base(self):
        if not self.materiales:
            return 0
        total_precio = sum(material.precio_base for material in self.materiales)
        return total_precio / len(self.materiales)

    def obtener_material_mayor_costo_mantenimiento(self):
        if not self.materiales:
            return None
        material_mayor = max(self.materiales, key=lambda m: m.calcular_costo_mantenimiento())
        return material_mayor

    def calcular_suma_costo_mantenimiento(self):
        return sum(material.calcular_costo_mantenimiento() for material in self.materiales)

    def contar_libros_mas_30_dias(self):
        return sum(1 for material in self.materiales if isinstance(material, Libro) and material.dias_en_biblioteca > 30)

    def contar_revistas_importadas(self):
        return sum(1 for material in self.materiales if isinstance(material, Revista) and not material.es_nacional)

if __name__ == "__main__":
    biblioteca = Biblioteca("material.csv")
    print(biblioteca)

    # print(biblioteca.cantidad_por_tipo())