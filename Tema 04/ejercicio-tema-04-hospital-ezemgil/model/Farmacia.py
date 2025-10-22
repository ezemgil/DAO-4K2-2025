from model.Atencion import Atencion

class Farmacia(Atencion):
    def __init__(self, codigo_atencion, tipo_cobro, importe_medicamentos, cupon_descuento):
        super().__init__(codigo_atencion, tipo_cobro)
        self.__importe_medicamentos = importe_medicamentos
        self.__cupon_descuento = cupon_descuento
    
    def importe_a_cobrar(self):
        importe = self.__importe_medicamentos - self.__cupon_descuento
        if self.get_tipo_cobro() == 2:
            importe *= 1.3
        elif self.get_tipo_cobro() == 1:
            importe *= 0.95
        return importe

    def get_importe_medicamentos(self):
        return self.__importe_medicamentos

    def set_importe_medicamentos(self, importe_medicamentos):
        self.__importe_medicamentos = importe_medicamentos

    def get_cupon_descuento(self):
        return self.__cupon_descuento

    def set_cupon_descuento(self, cupon_descuento):
        self.__cupon_descuento = cupon_descuento

    def __str__(self):
        return (f"Farmacia({super().__str__()}, Importe medicamentos: {self.__importe_medicamentos}, "
                f"Cupon descuento: {self.__cupon_descuento})")