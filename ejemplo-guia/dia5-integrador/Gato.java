// Gato.java
public class Gato extends Mascota implements Cuidable {

    public Gato(String nombre, String raza, int edad) {
        super(nombre, raza, edad);
    }

    @Override
    public void mostrarInfo() {
        System.out.println("Gato -> " + toString());
    }

    @Override
    public String obtenerCuidados() {
        return getNombre() + " necesita su caja de arena limpia y rascador.";
    }
}
