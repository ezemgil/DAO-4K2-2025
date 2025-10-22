__author__ = "89765 Matías Gil"

# from model.Atencion import Atencion
from model.Farmacia import Farmacia
from model.Hospital import Hospital
from model.Medica import Medica
from model.Paciente import Paciente


def main():
    # Crear hospital
    hospital = Hospital("Hospital Central")

    # Crear pacientes
    paciente1 = Paciente(1, False)  # Corazón, No habitual
    paciente2 = Paciente(2, True)   # Pulmón, Habitual
    paciente3 = Paciente(3, True)   # Otros, Habitual

    # Crear atenciones médicas
    medica1 = Medica(101, 1, paciente1, 2000)  # efectivo, habitual
    medica2 = Medica(102, 2, paciente2, 2500)  # tarjeta, no habitual
    medica3 = Medica(103, 2, paciente3, 3000)  # tarjeta, habitual

    # Crear atenciones de farmacia
    farmacia1 = Farmacia(201, 1, 1500, 100)    # efectivo, con cupón
    farmacia2 = Farmacia(202, 2, 1800, 0)      # tarjeta, sin cupón

    # Agregar atenciones al hospital
    hospital.add_atencion(medica1)
    hospital.add_atencion(medica2)
    hospital.add_atencion(medica3)
    hospital.add_atencion(farmacia1)
    hospital.add_atencion(farmacia2)

    # Mostrar todas las atenciones y sus importes a cobrar
    print("Listado de atenciones e importes a cobrar:")
    for atencion in hospital.get_atenciones():
        print(atencion)
        print(f"Importe a cobrar: ${atencion.importe_a_cobrar():.2f}")
        print("-" * 40)

    # Importe total de atenciones médicas
    print(f"Importe total de atenciones médicas: ${hospital.importe_total_atencion_consulta():.2f}")

    # Importe promedio de atenciones médicas entre $2000 y $3000
    promedio = hospital.importe_promedio_atenciones(2000, 3000)
    print(f"Importe promedio de atenciones médicas entre $2000 y $3000: ${promedio:.2f}")

    # Código de la primera atención médica a paciente habitual
    codigo = hospital.codigo_primera_atencion_habitual()
    print(f"Código de la primera atención médica a paciente habitual: {codigo}")


if __name__ == "__main__":
    main()
