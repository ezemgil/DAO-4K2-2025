from abc import ABC, abstractmethod


class Empleado(ABC):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo_basico):
        self.tipo = tipo
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.sueldo_basico = sueldo_basico
    
    @abstractmethod
    def calcularSueldo(self):
        ...

    def __str__(self):
        tipo_str = {1: "Obrero", 2: "Administrativo", 3: "Vendedor"}.get(self.tipo, "Desconocido")
        return f"{tipo_str} - Legajo: {self.legajo}, Nombre: {self.nombre} {self.apellido}, Sueldo Básico: ${self.sueldo_basico}"


class Obrero(Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo_basico, dias_trabajados):
        super().__init__(tipo, legajo, nombre, apellido, sueldo_basico)
        self.dias_trabajados = dias_trabajados
    
    def calcularSueldo(self):
        return (self.sueldo_basico / 20) * self.dias_trabajados

    def __str__(self):
        return f"{super().__str__()}, Días trabajados: {self.dias_trabajados}"


class Administrativo(Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo_basico, cobra_presentismo):
        super().__init__(tipo, legajo, nombre, apellido, sueldo_basico)
        self.cobra_presentismo = cobra_presentismo

    def calcularSueldo(self):
        return self.sueldo_basico * 1.13 if self.cobra_presentismo else self.sueldo_basico

    def __str__(self):
        presentismo_str = "Sí" if self.cobra_presentismo else "No"
        return f"{super().__str__()}, Cobra presentismo: {presentismo_str}"


class Vendedor(Empleado):
    def __init__(self, tipo, legajo, nombre, apellido, sueldo_basico, importe_total_ventas):
        super().__init__(tipo, legajo, nombre, apellido, sueldo_basico)
        self.importe_total_ventas = importe_total_ventas
    
    def calcularSueldo(self):
        return self.sueldo_basico + (0.01 * self.importe_total_ventas)

    def __str__(self):
        return f"{super().__str__()}, Importe total ventas: {self.importe_total_ventas}"