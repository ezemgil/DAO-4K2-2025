class Ascensor:
    def __init__(self, piso_min, piso_max, capacidad):
        if piso_min > piso_max:
            raise ValueError("piso_min debe ser menor o igual que piso_max")
        if capacidad <= 0:
            raise ValueError("La capacidad debe ser mayor que cero")
        self.capacidad = capacidad
        self.piso_min = piso_min
        self.piso_max = piso_max
        self.piso_actual = 0
        if not (self.piso_min <= self.piso_actual <= self.piso_max):
            raise ValueError("El piso inicial 0 debe estar dentro del rango de pisos")
        self.personas = 0

    def ir_a_piso(self, piso):
        if self.piso_min <= piso <= self.piso_max:
            self.piso_actual = piso
            return True
        return False

    def subir(self, cantidad):
        if cantidad <= 0:
            return -1
        espacio_disponible = self.capacidad - self.personas
        if cantidad <= espacio_disponible:
            self.personas += cantidad
            return cantidad
        else:
            self.personas += espacio_disponible
            return espacio_disponible

    def bajar(self, cantidad):
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
        return f"Ascensor en piso {self.piso_actual}. Personas dentro: {self.personas}."
