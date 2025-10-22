import pytest
from figuras import Triangulo

@pytest.mark.parametrize(
	"lado1, lado2, lado3, expected_area, expected_perimeter",
	[
		(3, 4, 5, 6.0, 12),
		(5, 5, 8, 12.0, 18),
		(7, 10, 5, 16.25, 22),
	]
)
def test_triangulo_parametrized(lado1, lado2, lado3, expected_area, expected_perimeter):
	t = Triangulo(lado1, lado2, lado3)
	assert round(t.superficie(), 2) == round(expected_area, 2)
	assert t.perimetro() == expected_perimeter
