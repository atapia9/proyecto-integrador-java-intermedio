// Main.java
// Version resuelta del menu integrador (Dia 5) usando el tema "Mascotas".
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 5: Menu integrador (Mascotas) ===");

        Perro perro = new Perro("Firulais", "Labrador", 3);
        Gato gato = new Gato("Michi", "Siames", 2);
        perro.mostrarInfo();
        gato.mostrarInfo();
        System.out.println(perro.obtenerCuidados());
        System.out.println(gato.obtenerCuidados());

        Scanner teclado = new Scanner(System.in);
        GestorMascotas gestor = new GestorMascotas();
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
                System.out.print("Raza: ");
                String raza = teclado.nextLine();
                System.out.print("Edad: ");
                int edad = Integer.parseInt(teclado.nextLine());

                try {
                    gestor.agregar(new Mascota(nombre, raza, edad));
                    System.out.println("Mascota agregada correctamente.");
                } catch (DatoInvalidoException error) {
                    System.out.println("Error: " + error.getMessage());
                }

            } else if (opcion == 2) {
                System.out.println("Lista de mascotas:");
                gestor.listar();

            } else if (opcion == 3) {
                System.out.print("Nombre a buscar: ");
                String nombreBuscado = teclado.nextLine();
                Mascota encontrada = gestor.buscarPorNombre(nombreBuscado);
                if (encontrada != null) {
                    System.out.println("Encontrada: " + encontrada);
                } else {
                    System.out.println("No se encontro la mascota.");
                }

            } else if (opcion == 4) {
                System.out.println("Hasta luego.");

            } else {
                System.out.println("Opcion no valida.");
            }
        }

        teclado.close();
    }
}
