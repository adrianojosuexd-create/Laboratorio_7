import pytest

# ==========================================
# FASE 2 y 3: GREEN / REFACTOR
# Escribir el código mínimo para que pase y 
# refactorizar para mejor legibilidad/rendimiento.
# ==========================================
def es_primo(numero):
    if numero < 2:
        return False
    # Refactorización: en lugar de revisar todos los números, 
    # solo revisamos hasta la raíz cuadrada para que sea más rápido.
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# ==========================================
# FASE 1: RED
# Escribir primero el test unitario.
# (Se diseñan los casos de prueba antes que la lógica de arriba)
# ==========================================
def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(1) == False
    assert es_primo(29) == True
    assert es_primo(-5) == False