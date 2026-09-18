// Main.java
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 4: Excepciones (Mascotas) ===");

        GestorMascotas gestor = new GestorMascotas();

        try {
            gestor.agregar(new Mascota("Firulais", "Labrador", 3));
            System.out.println("Firulais agregado correctamente.");

            gestor.agregar(new Mascota("Fantasma", "Desconocida", -1));
            System.out.println("Este mensaje no se debe imprimir.");
        } catch (DatoInvalidoException error) {
            System.out.println("Error capturado: " + error.getMessage());
        }

        System.out.println("Lista final:");
        gestor.listar();
    }
}
