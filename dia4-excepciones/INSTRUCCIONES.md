# Día 4 — Excepciones propias

**Objetivo:** crear una excepción propia y lanzarla/capturarla cuando un dato no sea válido.

## Qué entregar

- `DatoInvalidoException.java` completo (constructor que reciba un mensaje).
- `GestorElementos.java` con `agregar()` validando el dato y lanzando la excepción si es inválido.
- `Main.java` con un `try`/`catch` que agregue un dato inválido a propósito y capture el error.
- Un commit con el mensaje exacto: `Dia 4: excepciones`

## Qué hacer

1. Abre `DatoInvalidoException.java` y completa el constructor usando `super(mensaje);` para que el mensaje de error se guarde correctamente.
2. Abre `GestorElementos.java`, método `agregar()`: antes de agregar el objeto a la lista, valida el dato numérico (por ejemplo, que `cantidad` no sea negativa). Si es inválido, lanza la excepción:
   ```java
   if (elemento.getCantidad() < 0) {
       throw new DatoInvalidoException("La cantidad no puede ser negativa");
   }
   ```
3. `Main.java` ya trae un bloque `try` que agrega un objeto válido y después uno inválido a propósito, y un `catch (DatoInvalidoException error)` que imprime `error.getMessage()`.

## Salida esperada en consola (ejemplo)

Con el tema "Mascotas" (ver `ejemplo-guia/dia4-excepciones`), validando que la edad no sea negativa:

```
=== Dia 4: Excepciones (Mascotas) ===
Firulais agregado correctamente.
Error capturado: La edad no puede ser negativa
Lista final:
Mascota: Firulais | Raza: Labrador | Edad: 3 anios
```

## Checklist

- [ ] `DatoInvalidoException` guarda correctamente el mensaje (usa `super(mensaje)`; `error.getMessage()` ya no regresa `null`).
- [ ] `agregar()` valida el dato y lanza la excepción cuando es inválido.
- [ ] `Main.java` captura la excepción con `try`/`catch` e imprime el mensaje de error, y el objeto inválido NO queda en la lista final.

## Si te atoras

Revisa la versión completa y resuelta en [ejemplo-guia/dia4-excepciones/](../ejemplo-guia/dia4-excepciones/).
