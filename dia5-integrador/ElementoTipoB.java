// ElementoTipoB.java
// Esta clase ya esta resuelta (de dias anteriores). No necesitas modificarla.
public class ElementoTipoB extends Elemento implements Interactuable {

    public ElementoTipoB(String nombre, String detalle, int cantidad) {
        super(nombre, detalle, cantidad);
    }

    @Override
    public void mostrarInfo() {
        System.out.println("ElementoTipoB -> " + toString());
    }

    @Override
    public String obtenerEstado() {
        return "ElementoTipoB activo: " + getNombre();
    }
}
