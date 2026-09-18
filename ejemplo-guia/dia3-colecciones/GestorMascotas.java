// GestorMascotas.java
import java.util.ArrayList;

public class GestorMascotas {

    private ArrayList<Mascota> lista;

    public GestorMascotas() {
        lista = new ArrayList<Mascota>();
    }

    public void agregar(Mascota mascota) {
        lista.add(mascota);
    }

    public void listar() {
        for (Mascota m : lista) {
            System.out.println(m);
        }
    }

    public Mascota buscarPorNombre(String nombreBuscado) {
        for (Mascota m : lista) {
            if (m.getNombre().equals(nombreBuscado)) {
                return m;
            }
        }
        return null;
    }

    public int contar() {
        return lista.size();
    }
}
