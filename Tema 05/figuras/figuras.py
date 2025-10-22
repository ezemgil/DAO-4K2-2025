from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def superficie(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        pass


class Circulo(Figura):
    def __init__(self, _radio):
        self._radio = _radio

    @property
    def radio(self):
        return self._radio

    def superficie(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def __str__(self):
        return f"Círculo de radio {self.radio}"


class Triangulo(Figura):
    def __init__(self, _lado1, _lado2, _lado3):
        self._lado1 = _lado1
        self._lado2 = _lado2
        self._lado3 = _lado3

    @property
    def lado1(self):
        return self._lado1

    @property
    def lado2(self):
        return self._lado2

    @property
    def lado3(self):
        return self._lado3

    def superficie(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def __str__(self):
        return f"Triángulo de lados {self.lado1}, {self.lado2}, {self.lado3}"
    

class Rectangulo(Figura):
    def __init__(self, _base, _altura):
        self._base = _base
        self._altura = _altura

    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    def superficie(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

    def __str__(self):
        return f"Rectángulo de base {self.base} y altura {self.altura}"