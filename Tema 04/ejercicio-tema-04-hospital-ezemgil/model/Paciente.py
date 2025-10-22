class Paciente:
    def __init__(self, sintoma, es_habitual):
        self.__sintoma = sintoma
        self.__es_habitual = es_habitual

    def get_es_habitual(self):
        return self.__es_habitual

    def set_es_habitual(self, es_habitual):
        self.__es_habitual = es_habitual

    def get_sintoma(self):
        return self.__sintoma

    def set_sintoma(self, sintoma):
        self.__sintoma = sintoma

    def __str__(self):
        return f"Paciente(Sintoma: {self.__sintoma}, Habitual: {self.__es_habitual})"