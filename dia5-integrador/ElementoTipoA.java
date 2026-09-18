// ElementoTipoA.java
// Esta clase ya esta resuelta (de dias anteriores). No necesitas modificarla.
public class ElementoTipoA extends Elemento implements Interactuable {

    public ElementoTipoA(String nombre, String detalle, int cantidad) {
        super(nombre, detalle, cantidad);
    }

    @Override
    public void mostrarInfo() {
        System.out.println("ElementoTipoA -> " + toString());
    }

    @Override
    public String obtenerEstado() {
        return "ElementoTipoA activo: " + getNombre();
    }
}
