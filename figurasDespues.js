// Clase abstracta base (OCP)
class Figura {
    calcularArea() {
        throw new Error("Este método debe ser implementado");
    }
}

// Clases específicas (SRP)
class Circulo extends Figura {
    constructor(radio) { super(); this.radio = radio; }
    calcularArea() { return Math.PI * (this.radio ** 2); }
}

class Rectangulo extends Figura {
    constructor(base, altura) { super(); this.base = base; this.altura = altura; }
    calcularArea() { return this.base * this.altura; }
}

// Nueva figura (OCP)
class Triangulo extends Figura {
    constructor(base, altura) { super(); this.base = base; this.altura = altura; }
    calcularArea() { return (this.base * this.altura) / 2; }
}