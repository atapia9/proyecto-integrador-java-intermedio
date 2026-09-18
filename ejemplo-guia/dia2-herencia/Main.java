// Main.java
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 2: Herencia e interfaz (Mascotas) ===");

        Perro perro = new Perro("Firulais", "Labrador", 3);
        Gato gato = new Gato("Michi", "Siames", 2);

        perro.mostrarInfo();
        gato.mostrarInfo();

        System.out.println(perro.obtenerCuidados());
        System.out.println(gato.obtenerCuidados());
    }
}
