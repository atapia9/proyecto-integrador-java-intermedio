// Main.java
// Programa principal del Dia 1.
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 1: Clase base ===");

        // TODO: Crea 3 objetos de la clase Elemento con datos DIFERENTES entre si
        Elemento elemento1 = new Elemento("Dato 1", "Detalle 1", 1);
        Elemento elemento2 = new Elemento("Dato 2", "Detalle 2", 2);
        Elemento elemento3 = new Elemento("Dato 3", "Detalle 3", 3);

        // TODO: Imprime los 3 objetos (usaran el metodo toString automaticamente)
        System.out.println(elemento1);
        System.out.println(elemento2);
        System.out.println(elemento3);
    }
}
