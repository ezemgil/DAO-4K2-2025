from model.Medica import Medica

class Hospital:
    def __init__(self, razon_social):
        self.__razon_social = razon_social
        self.__atenciones = []

    def get_razon_social(self):
        return self.__razon_social

    def set_razon_social(self, razon_social):
        self.__razon_social = razon_social

    def get_atenciones(self):
        return self.__atenciones

    def set_atenciones(self, atenciones):
        self.__atenciones = atenciones

    def agregar_atencion(self, atencion):
        self.__atenciones.append(atencion)

    def add_atencion(self, atencion):
        self.__atenciones.append(atencion)
    
    def importe_total_atencion_consulta(self):
        return sum(atencion.importe_a_cobrar() for atencion in self.__atenciones if isinstance(atencion, Medica))
    
    def importe_promedio_atenciones(self, min_importe, max_importe):
        atenciones_filtradas = [atencion for atencion in self.__atenciones if min_importe <= atencion.importe_a_cobrar() <= max_importe]
        if not atenciones_filtradas:
            return 0
        return sum(atencion.importe_a_cobrar() for atencion in atenciones_filtradas) / len(atenciones_filtradas)

    def codigo_primera_atencion_habitual(self):
        for atencion in self.__atenciones:
            if isinstance(atencion, Medica) and atencion.get_paciente_atendido().get_es_habitual():
                return atencion.get_codigo_atencion()
        return 0        

    def __str__(self):
        return f"Hospital: {self.__razon_social}, Total de atenciones: {len(self.__atenciones)}"