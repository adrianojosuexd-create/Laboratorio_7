// Mal diseño: No cumple OCP ni SRP
function calcularArea(tipo, ...args) {
    if (tipo === "circulo") {
        return 3.14159 * (args[0] ** 2);
    } else if (tipo === "rectangulo") {
        return args[0] * args[1];
    }
}