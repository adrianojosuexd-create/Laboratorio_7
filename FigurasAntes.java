public class FigurasAntes {
    // Mal diseño: No cumple OCP ni SRP
    public double calcularArea(String tipo, double... args) {
        if (tipo.equals("circulo")) {
            return 3.14159 * args[0] * args[0];
        } else if (tipo.equals("rectangulo")) {
            return args[0] * args[1];
        }
        return 0;
    }
}