# Rúbrica de evaluación

Puntaje total: **100 puntos**. Aprobación mínima: **60 puntos**.

Se evalúa cada día por separado, con el mismo criterio: **20 puntos por día × 5 días = 100 puntos**.

## Criterio por día (20 puntos)

| Criterio | Puntos | Descripción |
|---|---|---|
| Compila | 10 | El código de la carpeta del día compila sin errores con `javac`. Se verifica automáticamente con GitHub Actions (pestaña "Actions"). |
| Cumple la actividad | 7 | Se completaron los `TODO` indicados en el `INSTRUCCIONES.md` de ese día y el programa produce una salida coherente con lo pedido. |
| Commit con mensaje correcto | 3 | Existe un commit con el mensaje exacto indicado en [COMO-ENTREGAR.md](COMO-ENTREGAR.md) (ejemplo: `Dia 1: clase base`). |

## Detalle por día

### Día 1 — Clase base (20 pts)
- Compila (10 pts)
- La clase tiene 3 atributos privados, constructor, getters/setters y `toString()`; se crean e imprimen 3 objetos (7 pts)
- Commit `Dia 1: clase base` (3 pts)

### Día 2 — Herencia e interfaz (20 pts)
- Compila (10 pts)
- 2 subclases sobrescriben `mostrarInfo()`; 1 interfaz con un método implementado por ambas subclases (7 pts)
- Commit `Dia 2: herencia e interfaz` (3 pts)

### Día 3 — Colecciones (20 pts)
- Compila (10 pts)
- `ArrayList` con al menos 3 objetos; métodos `listar()` y `buscarPorNombre()` funcionando (7 pts)
- Commit `Dia 3: colecciones` (3 pts)

### Día 4 — Excepciones (20 pts)
- Compila (10 pts)
- Excepción propia (`extends Exception`) que se lanza cuando un dato es inválido y se captura con `try`/`catch` (7 pts)
- Commit `Dia 4: excepciones` (3 pts)

### Día 5 — Integrador (20 pts)
- Compila (10 pts)
- Menú de consola con las 4 opciones (agregar, listar, buscar, salir) funcionando con las clases de los días anteriores; `ENTREGA.md` lleno (7 pts)
- Commit `Dia 5: menu integrador` (3 pts)

## Política de "compila primero"

Si un día **no compila**, automáticamente se obtienen 0 puntos de "Compila" y 0 de "Cumple la actividad" en ese día (no se puede evaluar una actividad que no se ejecuta), pero **sí** se otorgan los 3 puntos de commit si el mensaje es correcto. Por eso siempre es preferible entregar un `TODO` sin terminar (que compila con valores por defecto) que un intento roto que no compila.

## Escala final

| Puntos | Resultado |
|---|---|
| 60 – 100 | Aprobado |
| 0 – 59 | No aprobado (se recomienda reforzar y volver a intentar) |
