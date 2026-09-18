// Perro.java
public class Perro extends Mascota implements Cuidable {

    public Perro(String nombre, String raza, int edad) {
        super(nombre, raza, edad);
    }

    @Override
    public void mostrarInfo() {
        System.out.println("Perro -> " + toString());
    }

    @Override
    public String obtenerCuidados() {
        return getNombre() + " necesita paseos diarios y agua fresca.";
    }
}
