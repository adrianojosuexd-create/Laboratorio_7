import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class PrimosTest {
    
    // FASE 2 y 3: Implementación y refactorización
    public boolean esPrimo(int numero) {
        if (numero < 2) return false;
        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i == 0) return false;
        }
        return true;
    }

    // FASE 1: RED (Test)
    @Test
    public void testEsPrimo() {
        assertTrue(esPrimo(2));
        assertTrue(esPrimo(3));
        assertFalse(esPrimo(4));
        assertFalse(esPrimo(1));
        assertTrue(esPrimo(29));
        assertFalse(esPrimo(-5));
    }
}