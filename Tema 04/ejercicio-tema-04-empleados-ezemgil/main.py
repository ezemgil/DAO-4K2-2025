__author__ = "89765 Matías Gil"

from empleados import Empleado, Obrero, Administrativo, Vendedor


def cargar_empleados(ruta_archivo):
    empleados = []
    archivo = open(ruta_archivo)

    for empleado in archivo.readlines():
        datos = tuple(empleado[:-1].split(";"))

        if int(datos[0]) == 1: # Tipo: Obrero
            empleados.append(Obrero(int(datos[0]), datos[1], datos[2], datos[3], int(datos[4]), int(datos[5])))
        elif int(datos[0]) == 2: # Tipo: Administrativo
            empleados.append(Administrativo(int(datos[0]), datos[1], datos[2], datos[3], int(datos[4]), datos[5] == 'true'))
        elif int(datos[0]) == 3: # Tipo: Vendedor
            empleados.append(Vendedor(int(datos[0]), datos[1], datos[2], datos[3], int(datos[4]), int(datos[5])))
        else: # Tipo de empleado no soportado
            continue

    archivo.close()
    return empleados


def contar_empleados_por_tipo(empleados):
    conteo = {1: 0, 2: 0, 3: 0}  # 1: Obrero, 2: Administrativo, 3: Vendedor
    for empleado in empleados:
        if empleado.tipo in conteo:
            conteo[empleado.tipo] += 1
    return conteo


def buscar_empleado_por_legajo(empleados, legajo):
    for empleado in empleados:
        if empleado.legajo == legajo:
            return empleado
    return None


def main():
    empleados = cargar_empleados('./empleados.csv')

    # 1. Calcular el total a pagar de sueldos
    total = sum([empleado.calcularSueldo() for empleado in empleados])
    print(f"Total a pagar en sueldos: ${total:,.2f}")

    # 2. Contar los empleados por tipo (tres totales)
    conteo = contar_empleados_por_tipo(empleados)
    print(f"Cantidad de Obreros: {conteo[1]}")
    print(f"Cantidad de Administrativos: {conteo[2]}")
    print(f"Cantidad de Vendedores: {conteo[3]}")

    # 3. Buscar empleado por legajo y mostrar el sueldo a pagar
    legajo_a_buscar = input("Ingrese el legajo del empleado a buscar: ")
    empleado_encontrado = buscar_empleado_por_legajo(empleados, legajo_a_buscar)

    if empleado_encontrado:
        print("\nEmpleado encontrado: ")
        print(empleado_encontrado)
        print(f"Sueldo a pagar: ${empleado_encontrado.calcularSueldo():,.2f}")
    else:
        print(f"No se encontró un empleado con legajo {legajo_a_buscar}")


if __name__ == "__main__":
    main()    
