// Interfaz abstracta (OCP)
interface Figura {
    double calcularArea();
}

// Clases específicas (SRP)
class Circulo implements Figura {
    private double radio;
    public Circulo(double radio) { this.radio = radio; }
    public double calcularArea() { return Math.PI * radio * radio; }
}

class Rectangulo implements Figura {
    private double base, altura;
    public Rectangulo(double base, double altura) { this.base = base; this.altura = altura; }
    public double calcularArea() { return base * altura; }
}

// Nueva figura añadida sin modificar el resto (OCP)
class Triangulo implements Figura {
    private double base, altura;
    public Triangulo(double base, double altura) { this.base = base; this.altura = altura; }
    public double calcularArea() { return (base * altura) / 2; }
}