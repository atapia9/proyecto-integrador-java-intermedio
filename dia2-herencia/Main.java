// Main.java
// Programa principal del Dia 2.
public class Main {
    public static void main(String[] args) {
        System.out.println("=== Dia 2: Herencia e interfaz ===");

        // TODO: Crea un objeto de ElementoTipoA y otro de ElementoTipoB
        ElementoTipoA objetoA = new ElementoTipoA("Dato A", "Detalle A", 1);
        ElementoTipoB objetoB = new ElementoTipoB("Dato B", "Detalle B", 2);

        // TODO: Llama a mostrarInfo() en cada objeto
        objetoA.mostrarInfo();
        objetoB.mostrarInfo();

        // TODO (opcional): cuando ya hayas agregado el metodo en Interactuable
        // y lo hayas implementado en ambas subclases, prueba llamarlo aqui, por ejemplo:
        // System.out.println(objetoA.obtenerEstado());
        // System.out.println(objetoB.obtenerEstado());
    }
}
