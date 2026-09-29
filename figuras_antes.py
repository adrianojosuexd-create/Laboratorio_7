# Mal diseño: No cumple con la Responsabilidad Única ni está abierto a extensión.
def calcular_area(tipo, *args):
    if tipo == "circulo":
        return 3.14159 * (args[0] ** 2)
    elif tipo == "rectangulo":
        return args[0] * args[1]

print("Área circulo:", calcular_area("circulo", 5))