// Elemento.java
// Esta clase ya esta resuelta (de los dias anteriores). No necesitas modificarla.
public class Elemento {

    private String nombre;
    private String detalle;
    private int cantidad;

    public Elemento(String nombre, String detalle, int cantidad) {
        this.nombre = nombre;
        this.detalle = detalle;
        this.cantidad = cantidad;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDetalle() {
        return detalle;
    }

    public void setDetalle(String detalle) {
        this.detalle = detalle;
    }

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        this.cantidad = cantidad;
    }

    @Override
    public String toString() {
        return nombre + " | " + detalle + " | " + cantidad;
    }

    public void mostrarInfo() {
        System.out.println("Elemento: " + toString());
    }
}
