class Persona:
    def __init__(self, doc, nombre, apellido, edad):
        self.doc = doc
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return f"Nombre completo: {self.apellido}, {self.nombre}. Documento: {self.doc}. Edad: {self.edad} años."


def cargar_persona():
    doc = pedir_entero_positivo("Documento: ")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = pedir_entero_positivo("Edad: ")
    return Persona(doc, nombre, apellido, edad)


def pedir_entero_positivo(msj):
    while True:
        try:
            num = int(input(msj))
            if num > 0:
                return num
            else:
                print("(!) Error: El número debe ser positivo.\n")
        except:
            print("(!) Error: Debe ingresar un número entero.\n")


def main():
    n = int(input("Ingrese el número de personas a cargar: "))
    menor = None

    for i in range(n):
        print(f"\nPersona no.{i + 1}:")
        persona = cargar_persona()
        print(persona)

        if menor is None:
            menor = persona

        if persona.edad < menor.edad:
            menor = persona
        
    print(f"\nLa persona de menor edad es {menor}")
    

if __name__ == '__main__':
    main()
        

        

    
