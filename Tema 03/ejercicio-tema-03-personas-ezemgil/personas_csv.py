class Persona:
    def __init__(self, doc, nombre, apellido, edad):
        self.doc = doc
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"Nombre completo: {self.apellido}, {self.nombre}. Documento: {self.doc}. Edad: {self.edad} años."
    

def cargar_personas_dict(personas_csv, tiene_encabezado=False):
    personas = {}

    with open(personas_csv, encoding='utf8') as csv:
        if tiene_encabezado:
            next(csv)

        for linea in csv:
            datos_persona = linea.strip().split(",")
            doc, nombre, apellido, edad = datos_persona
            persona = Persona(int(doc), nombre, apellido, int(edad))
            personas[doc] = persona

    return personas


def es_vocal(letra):
    return letra.lower() in "aeiou"


def main():
    ruta_archivo = 'personas.csv'
    personas = cargar_personas_dict(ruta_archivo)
    print(f"Informes del archivo {ruta_archivo}:\n")
    
    # 1 | Cantidad de personas cargadas
    print(f"1. Cantidad de personas: {len(personas)}")

    # 2 | Cantidad de personas mayores de edad
    mayores = sum(1 for p in personas.values() if p.edad >= 18)
    print(f"2. Cantidad de personas mayores de edad: {mayores}")

    # 3 | Listado de nombres y apellidos donde el apellido empieza por vocal
    print("3. Listado de personas cuyo apellido empiezan por vocal:")
    for p in personas.values():
        if es_vocal(p.apellido[0]):
            print(f"\t- {p.apellido} {p.nombre}")
    print()
    
    # 4 | Cantidad de personas por cada apellido
    print("4. Cantidad de personas por cada apellido")
    apellidos = {}
    for p in personas.values():
        apellidos[p.apellido] = apellidos.get(p.apellido, 0) + 1


    for apellido, cantidad in apellidos.items():
        print(f"  - {apellido:<{15 + 2}} | {cantidad:>3}")



if __name__ == '__main__':
    main()