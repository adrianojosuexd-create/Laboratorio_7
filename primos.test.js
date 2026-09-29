// Implementación (GREEN/REFACTOR)
function esPrimo(numero) {
    if (numero < 2) return false;
    for (let i = 2; i <= Math.sqrt(numero); i++) {
        if (numero % i === 0) return false;
    }
    return true;
}

// Pruebas (RED)
test('Comprobación de números primos', () => {
    expect(esPrimo(2)).toBe(true);
    expect(esPrimo(3)).toBe(true);
    expect(esPrimo(4)).toBe(false);
    expect(esPrimo(1)).toBe(false);
    expect(esPrimo(29)).toBe(true);
    expect(esPrimo(-5)).toBe(false);
});