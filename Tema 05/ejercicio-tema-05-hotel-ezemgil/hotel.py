from abc import ABC, abstractmethod

class Hotel:
    def __init__(self, habitaciones_csv):
        self.habitaciones = []
        self.cargar_habitaciones(habitaciones_csv)

    def cargar_habitaciones(self, habitaciones_csv):
        with open(habitaciones_csv, 'r') as file:
            for linea in file:
                datos = linea.strip().split(',')
                tipo = int(datos[0])
                numero = int(datos[1])
                huesped = datos[2]
                costo_base = float(datos[3])
                noches = int(datos[4])

                if tipo == 1:
                    self.habitaciones.append(Estandar(numero, huesped, costo_base, noches))
                elif tipo == 2:
                    vista_mar = datos[5].strip().lower() == 'true'
                    self.habitaciones.append(Suite(numero, huesped, costo_base, noches, vista_mar))
                elif tipo == 3:
                    jacuzzi = datos[5].strip().lower() == 'true'
                    self.habitaciones.append(SuitePremium(numero, huesped, costo_base, noches, jacuzzi))

    def cantidad_por_tipo(self):
        return {
            "Estandar": sum(1 for h in self.habitaciones if type(h).__name__ == 'Estandar'),
            "Suite": sum(1 for h in self.habitaciones if type(h).__name__ == 'Suite'),
            "SuitePremium": sum(1 for h in self.habitaciones if type(h).__name__ == 'SuitePremium')
        }

    def cantidad_habitaciones(self):
        return len(self.habitaciones)

    def obtener_suma_reservas(self):
        return sum(h.calcular_costo() for h in self.habitaciones)

    def calcular_ingreso_total(self):
        return self.obtener_suma_reservas()

    def obtener_reserva_mas_cara(self):
        if not self.habitaciones:
            return None
        return max(self.habitaciones, key=lambda h: h.calcular_costo())

    def contar_suites_vista_mar(self):
        return sum(1 for h in self.habitaciones if isinstance(h, Suite) and h.vista_mar)

    def contar_suites_premium_jacuzzi(self):
        return sum(1 for h in self.habitaciones if isinstance(h, SuitePremium) and h.jacuzzi)

    def __str__(self):
        return "\n".join(str(habitacion) for habitacion in self.habitaciones)


class Habitacion(ABC):
    def __init__(self, tipo, numero, huesped, costo_base, noches):
        self._tipo = tipo
        self._numero = numero
        self._huesped = huesped
        self._costo_base = costo_base
        self._noches = noches

    @property
    def tipo(self):
        return self._tipo

    @property
    def numero(self):
        return self._numero

    @property
    def huesped(self):
        return self._huesped

    @property
    def costo_base(self):
        return self._costo_base

    @property
    def noches(self):
        return self._noches

    def calcular_costo_total(self):
        return self.calcular_costo()

    def __str__(self):
        return f"Tipo: {self._tipo}, Número: {self._numero}, Huésped: {self._huesped}, Costo Base: {self._costo_base}, Noches: {self._noches}"

    @abstractmethod
    def calcular_costo(self):
        ...


class Estandar(Habitacion):
    def __init__(self, numero, huesped, costo_base, noches, descuento=False):
        super().__init__(1, numero, huesped, costo_base, noches)
        self._descuento = descuento

    def __str__(self):
        return super().__str__()

    def calcular_costo(self):
        return self._costo_base * self._noches


class Suite(Habitacion):
    def __init__(self, numero, huesped, costo_base, noches, vista_mar):
        super().__init__(2, numero, huesped, costo_base, noches)
        self._vista_mar = vista_mar

    @property
    def vista_mar(self):
        return self._vista_mar

    def __str__(self):
        return super().__str__() + f", Vista al Mar: {self._vista_mar}"

    def calcular_costo(self):
        costo = self._costo_base * self._noches
        if self._vista_mar:
            costo *= 1.1
        return costo


class SuitePremium(Habitacion):
    def __init__(self, numero, huesped, costo_base, noches, jacuzzi):
        super().__init__(3, numero, huesped, costo_base, noches)
        self._jacuzzi = jacuzzi

    @property
    def jacuzzi(self):
        return self._jacuzzi

    def __str__(self):
        return super().__str__() + f", Jacuzzi: {self._jacuzzi}"

    def calcular_costo(self):
        costo = self._costo_base * self._noches
        if self._jacuzzi:
            costo *= 1.2
        return costo