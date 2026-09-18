// Elemento.java
// Clase base generica del proyecto integrador.
// TODO: Renombra esta clase segun la opcion que elegiste (ver OPCIONES.md):
//   Opcion A (Biblioteca) -> Material
//   Opcion B (Tienda)     -> Producto
//   Opcion C (Escuela)    -> Persona
// (Recuerda: si renombras la clase, el archivo tambien debe renombrarse igual)
public class Elemento {

    // ---------- Atributos privados ----------
    // Cada opcion usa nombres distintos para estos 3 datos, por ejemplo:
    //   Opcion A (Material): titulo, autor, anio
    //   Opcion B (Producto): nombre, precio, existencia
    //   Opcion C (Persona):  nombre, edad, correo
    // TODO: Renombra los atributos y ajusta el tipo si tu opcion lo requiere
    private String nombre;
    private String detalle;
    private int cantidad;

    // ---------- Constructor ----------
    // TODO: Completa el constructor asignando cada parametro a su atributo
    public Elemento(String nombre, String detalle, int cantidad) {
        // TODO: asigna nombre al atributo nombre -> this.nombre = nombre;

        // TODO: asigna detalle al atributo detalle -> this.detalle = detalle;

        // TODO: asigna cantidad al atributo cantidad -> this.cantidad = cantidad;
    }

    // ---------- Getters y setters ----------

    public String getNombre() {
        // TODO: retorna el valor real del atributo nombre
        return "TODO: falta implementar getNombre()";
    }

    public void setNombre(String nombre) {
        // TODO: asigna el parametro al atributo nombre
    }

    public String getDetalle() {
        // TODO: retorna el valor real del atributo detalle
        return "TODO: falta implementar getDetalle()";
    }

    public void setDetalle(String detalle) {
        // TODO: asigna el parametro al atributo detalle
    }

    public int getCantidad() {
        // TODO: retorna el valor real del atributo cantidad
        return 0;
    }

    public void setCantidad(int cantidad) {
        // TODO: asigna el parametro al atributo cantidad
    }

    // ---------- toString ----------
    @Override
    public String toString() {
        // TODO: retorna un texto legible con los 3 atributos, por ejemplo:
        // return nombre + " | " + detalle + " | " + cantidad;
        return "TODO: falta implementar toString()";
    }
}
