# Día 1 — Clase base

**Objetivo:** crear una clase con atributos privados, constructor, getters/setters y `toString()`.

## Qué entregar

- El archivo `Elemento.java` con los 3 atributos, el constructor y los métodos `get`/`set` completos.
- El archivo `Main.java` creando 3 objetos con datos distintos y mostrándolos con `System.out.println`.
- Un commit con el mensaje exacto: `Dia 1: clase base`

## Qué hacer

1. Abre `Elemento.java`. Si quieres, cambia el nombre de los atributos según tu opción elegida (ver [OPCIONES.md](../OPCIONES.md)); renombrar es opcional.
2. Completa el constructor: cada parámetro se debe guardar en su atributo (`this.atributo = atributo;`).
3. Completa cada `get` (debe regresar el valor del atributo) y cada `set` (debe asignar el valor recibido al atributo).
4. Completa `toString()` para que regrese un texto legible con los 3 datos.
5. Abre `Main.java` y crea 3 objetos con datos diferentes; imprime cada uno.

## Salida esperada en consola (ejemplo)

Con el tema "Mascotas" (ver `ejemplo-guia/dia1-clase-base`), la salida se ve así:

```
=== Dia 1: Clase base (Mascotas) ===
Mascota: Firulais | Raza: Labrador | Edad: 3 anios
Mascota: Michi | Raza: Siames | Edad: 2 anios
Mascota: Rocky | Raza: Bulldog | Edad: 5 anios
```

Tu salida se verá parecida, pero con los datos de tu propia opción (A, B o C).

## Checklist

- [ ] `Elemento.java` compila y los 3 getters ya regresan el dato real (no el texto "TODO...").
- [ ] `Main.java` crea 3 objetos con datos DIFERENTES entre sí.
- [ ] Al ejecutar `java Main`, se imprimen los 3 objetos con datos legibles (no salen vacíos ni con "TODO").

## Si te atoras

Revisa la versión completa y resuelta en [ejemplo-guia/dia1-clase-base/](../ejemplo-guia/dia1-clase-base/). También puedes leer [docs/COMPILAR-Y-EJECUTAR.md](../docs/COMPILAR-Y-EJECUTAR.md) si el error es al compilar.
