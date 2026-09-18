// GestorElementos.java
// Esta clase ya esta resuelta (de dias anteriores). No necesitas modificarla.
import java.util.ArrayList;

public class GestorElementos {

    private ArrayList<Elemento> lista;

    public GestorElementos() {
        lista = new ArrayList<Elemento>();
    }

    public void agregar(Elemento elemento) throws DatoInvalidoException {
        if (elemento.getCantidad() < 0) {
            throw new DatoInvalidoException("La cantidad no puede ser negativa");
        }
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
