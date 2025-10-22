class Auto:
    def __init__(self, combustible_actual):
        self.combustible_actual = combustible_actual
        self.capacidad_max = 49
        self.reserva = 5

    def __str__(self):
        return f"Auto con {self.combustible_actual} lt de {self.capacidad_max} lt de combustible. Reserva: {self.reserva}"

    def conducir(self, distancia):
        # ¿Puede recorrer la distancia?
        distancia_recorrible = self.combustible_actual * 11
        if not distancia_recorrible >= distancia:
            # No, no puedo recorrer
            return False

        # Sí, puedo recorrer
        litros_utilizados = distancia / 11
        self.combustible_actual -= litros_utilizados
        return True

    def cargar_combustible(self, cantidad_cargar):
        capacidad_actual = (self.capacidad_max + self.reserva) - self.combustible_actual

        if cantidad_cargar > capacidad_actual:
            # Derramo combustible, ya que supera la capacidad del tanque
            combustible_derramado = cantidad_cargar - capacidad_actual
            return combustible_derramado
        
        # No derramo combustible
        return 0

