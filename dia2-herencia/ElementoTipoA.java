// ElementoTipoA.java
// TODO: Renombra esta clase segun tu opcion, por ejemplo: Libro / Alimento / Alumno
public class ElementoTipoA extends Elemento implements Interactuable {

    public ElementoTipoA(String nombre, String detalle, int cantidad) {
        super(nombre, detalle, cantidad);
    }

    // TODO: Sobrescribe (override) el metodo mostrarInfo() heredado de Elemento
    @Override
    public void mostrarInfo() {
        // TODO: imprime informacion especifica de este tipo, por ejemplo:
        // System.out.println("Soy un Libro: " + toString());
    }

    // TODO: Una vez que agregues el metodo en Interactuable.java, impleméntalo aqui.
    // Recuerda escribir @Override arriba del metodo y usar la MISMA firma (nombre,
    // parametros y tipo de retorno) que declaraste en la interfaz.

}
