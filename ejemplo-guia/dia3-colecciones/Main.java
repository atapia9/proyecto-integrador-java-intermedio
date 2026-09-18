// Main.java
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 3: Colecciones (Mascotas) ===");

        GestorMascotas gestor = new GestorMascotas();
        gestor.agregar(new Mascota("Firulais", "Labrador", 3));
        gestor.agregar(new Mascota("Michi", "Siames", 2));
        gestor.agregar(new Mascota("Rocky", "Bulldog", 5));

        System.out.println("Lista completa:");
        gestor.listar();

        System.out.println("Buscando a Michi:");
        Mascota encontrada = gestor.buscarPorNombre("Michi");
        if (encontrada != null) {
            System.out.println("Encontrada: " + encontrada);
        } else {
            System.out.println("No se encontro la mascota.");
        }
    }
}
