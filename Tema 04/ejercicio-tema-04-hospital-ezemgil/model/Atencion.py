from abc import ABC, abstractmethod

class Atencion(ABC):
    def __init__(self, codigo_atencion, tipo_cobro):
        self.__codigo_atencion = codigo_atencion
        self.__tipo_cobro = tipo_cobro

    @abstractmethod
    def importe_a_cobrar(self):
        ...

    def get_codigo_atencion(self):
        return self.__codigo_atencion

    def set_codigo_atencion(self, codigo_atencion):
        self.__codigo_atencion = codigo_atencion

    def get_tipo_cobro(self):
        return self.__tipo_cobro

    def set_tipo_cobro(self, tipo_cobro):
        self.__tipo_cobro = tipo_cobro

    def __str__(self):
        return f"Código: {self.__codigo_atencion}, Tipo cobro: {self.__tipo_cobro}"