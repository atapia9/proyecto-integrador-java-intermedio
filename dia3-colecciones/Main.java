// Main.java
// Programa principal del Dia 3.
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 3: Colecciones (ArrayList) ===");

        GestorElementos gestor = new GestorElementos();

        // TODO: Agrega al menos 3 objetos Elemento al gestor
        gestor.agregar(new Elemento("Dato 1", "Detalle 1", 1));
        gestor.agregar(new Elemento("Dato 2", "Detalle 2", 2));
        gestor.agregar(new Elemento("Dato 3", "Detalle 3", 3));

        System.out.println("Lista completa:");
        gestor.listar();

        // TODO: Busca un elemento por nombre y muestra el resultado
        Elemento encontrado = gestor.buscarPorNombre("Dato 1");
        if (encontrado != null) {
            System.out.println("Encontrado: " + encontrado);
        } else {
            System.out.println("No se encontro el elemento.");
        }
    }
}
