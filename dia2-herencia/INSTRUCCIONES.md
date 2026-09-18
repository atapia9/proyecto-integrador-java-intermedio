# Día 2 — Herencia e interfaz

**Objetivo:** crear 2 subclases que sobrescriban un método, y una interfaz que ambas implementen.

## Qué entregar

- `Interactuable.java` con un método abstracto declarado.
- `ElementoTipoA.java` y `ElementoTipoB.java`, ambas heredando de `Elemento`, sobrescribiendo `mostrarInfo()` e implementando el método de `Interactuable`.
- Un commit con el mensaje exacto: `Dia 2: herencia e interfaz`

## Qué hacer

1. La clase `Elemento.java` de esta carpeta ya viene resuelta (es la del Día 1); no necesitas modificarla.
2. Abre `Interactuable.java` y declara **un** método (por ejemplo `String obtenerEstado();`). Revisa los ejemplos en el comentario del archivo.
3. Abre `ElementoTipoA.java`:
   - Completa `mostrarInfo()` para que imprima información específica de este tipo.
   - Agrega `@Override` e implementa el método que declaraste en `Interactuable`.
4. Repite el paso 3 en `ElementoTipoB.java`.
5. En `Main.java`, ya se crea un objeto de cada subclase y se llama a `mostrarInfo()`. Si quieres, agrega también una llamada al método de la interfaz.

## Salida esperada en consola (ejemplo)

Con el tema "Mascotas" (ver `ejemplo-guia/dia2-herencia`):

```
=== Dia 2: Herencia e interfaz (Mascotas) ===
Perro -> Mascota: Firulais | Raza: Labrador | Edad: 3 anios
Gato -> Mascota: Michi | Raza: Siames | Edad: 2 anios
Firulais necesita paseos diarios y agua fresca.
Michi necesita su caja de arena limpia y rascador.
```

## Checklist

- [ ] `Interactuable` tiene un método declarado (ya no está vacía).
- [ ] `ElementoTipoA` y `ElementoTipoB` sobrescriben `mostrarInfo()` con información distinta cada una.
- [ ] Ambas clases implementan el método de `Interactuable` con `@Override`.

## Si te atoras

Revisa la versión completa y resuelta en [ejemplo-guia/dia2-herencia/](../ejemplo-guia/dia2-herencia/).
