// Main.java
// Programa principal del Dia 5: menu integrador.
// Todas las demas clases de esta carpeta (Elemento, ElementoTipoA, ElementoTipoB,
// Interactuable, GestorElementos, DatoInvalidoException) ya vienen resueltas de
// los dias anteriores. Tu trabajo aqui es conectar el menu con el GestorElementos.
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 5: Menu integrador ===");

        // Pequena demostracion de lo visto en el Dia 2 (herencia + interfaz)
        ElementoTipoA objetoA = new ElementoTipoA("Dato A", "Detalle A", 1);
        ElementoTipoB objetoB = new ElementoTipoB("Dato B", "Detalle B", 2);
        objetoA.mostrarInfo();
        objetoB.mostrarInfo();

        Scanner teclado = new Scanner(System.in);
        GestorElementos gestor = new GestorElementos();
        int opcion = 0;

        while (opcion != 4) {
            System.out.println("");
            System.out.println("===== MENU =====");
            System.out.println("1) Agregar");
            System.out.println("2) Listar");
            System.out.println("3) Buscar por nombre");
            System.out.println("4) Salir");
            System.out.print("Elige una opcion: ");

            opcion = Integer.parseInt(teclado.nextLine());

            if (opcion == 1) {
                System.out.print("Nombre: ");
                String nombre = teclado.nextLine();
                System.out.print("Detalle: ");
                String detalle = teclado.nextLine();
                System.out.print("Cantidad: ");
                int cantidad = Integer.parseInt(teclado.nextLine());

                try {
                    // TODO: llama aqui a gestor.agregar(new Elemento(nombre, detalle, cantidad));
                    System.out.println("TODO: falta llamar a gestor.agregar()");
                } catch (Exception error) {
                    System.out.println("Error: " + error.getMessage());
                }

            } else if (opcion == 2) {
                // TODO: llama aqui a gestor.listar();
                System.out.println("TODO: falta llamar a gestor.listar()");

            } else if (opcion == 3) {
                System.out.print("Nombre a buscar: ");
                String nombreBuscado = teclado.nextLine();
                // TODO: llama a gestor.buscarPorNombre(nombreBuscado) y muestra el resultado
                // (si regresa null, avisa que no se encontro)
                System.out.println("TODO: falta llamar a gestor.buscarPorNombre()");

            } else if (opcion == 4) {
                System.out.println("Hasta luego.");

            } else {
                System.out.println("Opcion no valida.");
            }
        }

        teclado.close();
    }
}
