// GestorElementos.java
// Clase que administra una lista (ArrayList) de objetos Elemento.
// A partir de este dia, agregar() valida el dato antes de guardarlo.
import java.util.ArrayList;

public class GestorElementos {

    private ArrayList<Elemento> lista;

    public GestorElementos() {
        lista = new ArrayList<Elemento>();
    }

    // Ya viene con "throws DatoInvalidoException" en la firma: eso permite que este
    // metodo pueda lanzar la excepcion. Tu trabajo es agregar la validacion adentro.
    public void agregar(Elemento elemento) throws DatoInvalidoException {
        // TODO: antes de agregar, valida que "cantidad" no sea negativa.
        // Si es invalida, lanza la excepcion, por ejemplo:
        // if (elemento.getCantidad() < 0) {
        //     throw new DatoInvalidoException("La cantidad no puede ser negativa");
        // }
        lista.add(elemento);
    }

    public void listar() {
        for (Elemento e : lista) {
            System.out.println(e);
        }
    }

    public Elemento buscarPorNombre(String nombreBuscado) {
        for (Elemento e : lista) {
            if (e.getNombre().equals(nombreBuscado)) {
                return e;
            }
        }
        return null;
    }

    public int contar() {
        return lista.size();
    }
}
