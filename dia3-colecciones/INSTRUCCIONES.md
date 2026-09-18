# Día 3 — Colecciones (ArrayList)

**Objetivo:** guardar varios objetos en un `ArrayList` y poder listarlos y buscarlos por nombre.

## Qué entregar

- `GestorElementos.java` con `agregar()`, `listar()` y `buscarPorNombre()` completos.
- `Main.java` agregando al menos 3 objetos y probando `listar()` y `buscarPorNombre()`.
- Un commit con el mensaje exacto: `Dia 3: colecciones`

## Qué hacer

1. `Elemento.java` ya viene resuelto de los días anteriores.
2. Abre `GestorElementos.java`:
   - En `agregar(Elemento elemento)`, agrega el objeto a la lista (`lista.add(elemento);`).
   - En `listar()`, recorre la lista con un `for` e imprime cada elemento.
   - En `buscarPorNombre(String nombreBuscado)`, recorre la lista y compara con `.equals(nombreBuscado)`; si encuentras coincidencia, regresa ese objeto; si terminas el ciclo sin encontrar nada, regresa `null`.
3. En `Main.java`, ya se agregan 3 objetos de ejemplo; puedes cambiarlos por los tuyos. Se llama a `listar()` y a `buscarPorNombre()` con un nombre que exista.

## Salida esperada en consola (ejemplo)

Con el tema "Mascotas" (ver `ejemplo-guia/dia3-colecciones`):

```
=== Dia 3: Colecciones (Mascotas) ===
Lista completa:
Mascota: Firulais | Raza: Labrador | Edad: 3 anios
Mascota: Michi | Raza: Siames | Edad: 2 anios
Mascota: Rocky | Raza: Bulldog | Edad: 5 anios
Buscando a Michi:
Encontrada: Mascota: Michi | Raza: Siames | Edad: 2 anios
```

## Checklist

- [ ] `agregar()` guarda el objeto en el `ArrayList` (la lista crece con cada llamada).
- [ ] `listar()` imprime todos los objetos guardados, uno por línea (ya no muestra el mensaje "TODO...").
- [ ] `buscarPorNombre()` regresa el objeto correcto si existe, y `null` si no existe.

## Si te atoras

Revisa la versión completa y resuelta en [ejemplo-guia/dia3-colecciones/](../ejemplo-guia/dia3-colecciones/).
