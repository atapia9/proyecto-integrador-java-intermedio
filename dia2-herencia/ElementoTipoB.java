// ElementoTipoB.java
// TODO: Renombra esta clase segun tu opcion, por ejemplo: Revista / Electronico / Profesor
public class ElementoTipoB extends Elemento implements Interactuable {

    public ElementoTipoB(String nombre, String detalle, int cantidad) {
        super(nombre, detalle, cantidad);
    }

    // TODO: Sobrescribe (override) el metodo mostrarInfo() heredado de Elemento
    @Override
    public void mostrarInfo() {
        // TODO: imprime informacion especifica de este tipo, por ejemplo:
        // System.out.println("Soy una Revista: " + toString());
    }

    // TODO: Una vez que agregues el metodo en Interactuable.java, impleméntalo aqui.
    // Recuerda escribir @Override arriba del metodo y usar la MISMA firma (nombre,
    // parametros y tipo de retorno) que declaraste en la interfaz.

}
