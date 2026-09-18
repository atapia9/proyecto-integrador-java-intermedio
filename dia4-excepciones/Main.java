// Main.java
// Programa principal del Dia 4.
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 4: Excepciones ===");

        GestorElementos gestor = new GestorElementos();

        // TODO: Usa try/catch para agregar elementos, incluyendo un dato invalido a
        // proposito (por ejemplo, cantidad negativa) para comprobar que se captura el error.
        try {
            gestor.agregar(new Elemento("Dato 1", "Detalle 1", 1));
            System.out.println("Dato 1 agregado correctamente.");

            gestor.agregar(new Elemento("Dato invalido", "Detalle", -5));
            System.out.println("Este mensaje no se deberia imprimir si la validacion ya funciona.");
        } catch (DatoInvalidoException error) {
            System.out.println("Error capturado: " + error.getMessage());
        }

        System.out.println("Lista final:");
        gestor.listar();
    }
}
