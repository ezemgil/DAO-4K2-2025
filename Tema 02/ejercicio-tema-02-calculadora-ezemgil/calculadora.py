# Debe verse como:
# 1 - Suma
# 2 - Diferencia
# 3 - Producto
# 4 - Cociente

def mostrar_menu():
    print('\nCalculadora:')
    print('1 - Suma')
    print('2 - Diferencia')
    print('3 - Producto')
    print('4 - Cociente')


def suma(a, b):
    return a + b


def diferencia(a, b):
    return a - b


def producto(a, b):
    return a * b


def cociente(a, b):
    if b != 0:
        return a / b
    else:
        return 'Error: División por cero no permitida.'


def calcular():
    mostrar_menu()
    op = int(input('Ingrese la opción (0 para salir): '))
    while op != 0:
        if type(op) != int:
            print('Opción inválida, intente nuevamente')
        if op > 0 and op <= 4:
            a = float(input('Ingrese el primer número: '))
            b = float(input('Ingrese el segundo número: '))
            operaciones = [None, suma, diferencia, producto, cociente]
            resultado = operaciones[op](a, b)
            print(resultado)
        else:
            print('Opción inválida, intente nuevamente')
        op = int(input('Ingrese la opción (0 para salir): '))

    else:
        print('Programa finalizado')
        


if __name__ == '__main__':
    calcular()
