// GestorElementos.java
// Clase que administra una lista (ArrayList) de objetos Elemento.
import java.util.ArrayList;

public class GestorElementos {

    private ArrayList<Elemento> lista;

    public GestorElementos() {
        lista = new ArrayList<Elemento>();
    }

    // TODO: Agrega el objeto "elemento" a la lista
    public void agregar(Elemento elemento) {
        // TODO: lista.add(elemento);
    }

    // TODO: Recorre la lista e imprime cada elemento (uno por linea)
    public void listar() {
        // TODO: usa un for (Elemento e : lista) { System.out.println(e); }
        System.out.println("TODO: aun no se implementa listar()");
    }

    // TODO: Busca un elemento cuyo nombre coincida EXACTAMENTE con "nombreBuscado".
    // Si lo encuentra, lo regresa. Si no lo encuentra, regresa null.
    public Elemento buscarPorNombre(String nombreBuscado) {
        // TODO: recorre la lista, compara con e.getNombre().equals(nombreBuscado)
        // y regresa el que coincida.
        return null;
    }

    public int contar() {
        return lista.size();
    }
}
