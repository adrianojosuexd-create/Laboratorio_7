from abc import ABC, abstractmethod
import math

# Interfaz abstracta (Principio Open/Closed - Abierto a extensión, cerrado a modificación)
class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

# Clases específicas (Principio de Responsabilidad Única)
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura

# Añadimos una nueva figura sin modificar el código anterior
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return (self.base * self.altura) / 2

# Probando el código
circulo = Circulo(5)
triangulo = Triangulo(10, 5)

print(f"Área del círculo: {circulo.calcular_area():.2f}")
print(f"Área del triángulo: {triangulo.calcular_area():.2f}") 