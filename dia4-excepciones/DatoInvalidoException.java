// DatoInvalidoException.java
// Excepcion propia: se lanza cuando un dato no es valido (ejemplo: una cantidad negativa).
public class DatoInvalidoException extends Exception {

    // TODO: Completa el constructor para que reciba un mensaje y se lo pase a la clase padre
    public DatoInvalidoException(String mensaje) {
        // TODO: usa super(mensaje); para que el mensaje se guarde correctamente
        // (si dejas el constructor vacio, el programa compila pero getMessage()
        // regresara null en lugar de tu mensaje)
    }
}
