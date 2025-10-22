# DAO, clase 3 [20/08/2025]
from math import sqrt

def cuadrado(x):
    return x * x

def cubo(x):
    return x * x * x

def mitad(x):
    return x/2

# calcular = cubo
# print(calcular(9))

# calcular = mitad
# print(calcular(9))

# calcular = lambda x: x * 2
# print(calcular(9))

## Operación es una función
def calcular(valor, operacion):
    return operacion(valor)

# print(calcular(9, lambda x: x * 2))
# print(calcular(9, sqrt))

# calcular(9, print)


def recorrer_mostrar(v, funcion):
    # Recorre todo el vector, y cada valor de x lo asigna a 'funcion'
    # En álgebra: ∀x/x∈v
    for x in v:
        print(funcion(x))


def mapear(v, funcion):
    res = []
    for x in v:
        res.append(funcion(x))
    return res


numeros = [3, 8, 4, 122]
# recorrer_mostrar(numeros, lambda x: x ** 2)
# recorrer_mostrar(numeros, lambda x: x ** 2)
print(mapear(numeros, lambda x: x ** 2))
# mapear(numeros, sqrt)
