from model.Atencion import Atencion

class Medica(Atencion):
    def __init__(self, 
    codigo_atencion, tipo_cobro, paciente_atendido, importe_consulta):
        super().__init__(codigo_atencion, tipo_cobro)
        self.__paciente_atendido = paciente_atendido
        self.__importe_consulta = importe_consulta

    def importe_a_cobrar(self):
        importe = self.__importe_consulta * 0.75 if self.__paciente_atendido.get_es_habitual() else self.__importe_consulta
        if self.get_tipo_cobro() == 2:
            importe *= 1.2
        elif self.get_tipo_cobro() == 1:
            importe *= 0.9
        return importe

    def get_paciente_atendido(self):
        return self.__paciente_atendido

    def set_paciente_atendido(self, paciente_atendido):
        self.__paciente_atendido = paciente_atendido

    def get_importe_consulta(self):
        return self.__importe_consulta

    def set_importe_consulta(self, importe_consulta):
        self.__importe_consulta = importe_consulta

    def __str__(self):
        return (f"Medica({super().__str__()}, Paciente: {self.__paciente_atendido}, "
                f"Importe consulta: {self.__importe_consulta})")