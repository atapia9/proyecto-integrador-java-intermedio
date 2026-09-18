// Elemento.java
// Esta clase ya esta resuelta (es la clase base que se trabajo en el Dia 1).
// Tu tarea en el Dia 2 es crear las subclases y la interfaz (mas abajo en esta carpeta).
// TODO (opcional): si quieres, renombra esta clase segun tu opcion: Material / Producto / Persona
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

    // Metodo generico que las subclases sobrescribiran (override) con informacion propia
    public void mostrarInfo() {
        System.out.println("Elemento: " + toString());
    }
}
