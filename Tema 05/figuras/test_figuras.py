import pytest
from figuras import Circulo, Triangulo, Rectangulo

def test_circulo():
    c = Circulo(2)
    assert round(c.superficie(), 2) == round(3.141592653589793 * 4, 2)
    assert round(c.perimetro(), 2) == round(2 * 3.141592653589793 * 2, 2)

def test_triangulo():
    t = Triangulo(3, 4, 5)
    assert round(t.superficie(), 2) == 6.0
    assert t.perimetro() == 12

def test_rectangulo():
    r = Rectangulo(2, 6)
    assert r.superficie() == 12
    assert r.perimetro() == 16