class Ascensor:
    def __init__(self, capacidad, piso_min, piso_max):
        self.capacidad = capacidad
        self.piso_min = piso_min
        self.piso_max = piso_max
        self.piso_actual = piso_min
        self.personas = 0

    def ir_a_piso(self, piso):
        if self.piso_min <= piso <= self.piso_max:
            self.piso_actual = piso
            return True
        return False

    def subir_personas(self, cantidad):
        if cantidad <= 0:
            return -1
        espacio_disponible = self.capacidad - self.personas
        if cantidad <= espacio_disponible:
            self.personas += cantidad
            return cantidad
        else:
            self.personas += espacio_disponible
            return espacio_disponible

    def bajar_personas(self, cantidad):
        if cantidad <= 0:
            return -1
        if cantidad <= self.personas:
            self.personas -= cantidad
            return cantidad
        else:
            bajaron = self.personas
            self.personas = 0
            return bajaron

    def __str__(self):
        return f"Ascensor en piso {self.piso_actual} con {self.personas} personas adentro."


# Ejemplo de uso
ascensor = Ascensor(capacidad=5, piso_min=-2, piso_max=10)

print(ascensor)  # Estado inicial

print("Intento ir al piso 3:", ascensor.ir_a_piso(3))
print("Intento ir al piso 12:", ascensor.ir_a_piso(12))

print("Suben 3 personas:", ascensor.subir_personas(3))
print("Suben 4 personas:", ascensor.subir_personas(4))  # Solo entran 2

print(ascensor)

print("Bajan 2 personas:", ascensor.bajar_personas(2))
print("Bajan 5 personas:", ascensor.bajar_personas(5))

print(ascensor)
