# Opciones del proyecto

Elige **una sola opción** y úsala durante los 5 días. No mezcles opciones.

Los esqueletos de código (carpetas `diaN-...`) usan nombres genéricos: `Elemento`, `ElementoTipoA`, `ElementoTipoB`, `Interactuable`. La tabla de abajo muestra el nombre que le correspondería a cada clase según tu opción.

## Opción A — Biblioteca

- **Clase base:** `Material` — atributos: `titulo` (String), `autor` (String), `anio` (int)
- **Subclases:** `Libro`, `Revista`
- **Interfaz:** `Prestable` — ejemplo de método: `boolean estaDisponible();`

## Opción B — Tienda

- **Clase base:** `Producto` — atributos: `nombre` (String), `precio` (double), `existencia` (int)
- **Subclases:** `Alimento`, `Electronico`
- **Interfaz:** `Vendible` — ejemplo de método: `double calcularTotal();`

## Opción C — Escuela

- **Clase base:** `Persona` — atributos: `nombre` (String), `edad` (int), `correo` (String)
- **Subclases:** `Alumno`, `Profesor`
- **Interfaz:** `Evaluable` — ejemplo de método: `String evaluar();`

## Nota importante sobre los nombres

**Renombrar las clases genéricas es opcional, no obligatorio.** Si te sientes más cómodo dejando los nombres `Elemento`, `ElementoTipoA`, `ElementoTipoB` e `Interactuable` durante los 5 días, está perfectamente bien y no baja tu calificación: la rúbrica evalúa el **contenido** (atributos, herencia, interfaz, colección, excepción, menú), no los nombres de las clases.

Si decides renombrar, recuerda la regla de Java: **el nombre del archivo `.java` debe coincidir exactamente con el nombre de la clase pública que contiene** (por ejemplo, si renombras la clase a `Material`, el archivo debe llamarse `Material.java`). Si algo deja de compilar después de renombrar, siempre puedes regresar los nombres originales.

## ¿Dónde uso el nombre de mi opción?

Con que tus **atributos, subclases e interfaz representen el tema elegido** es suficiente (por ejemplo, que tus 3 atributos sean parecidos a `titulo`/`autor`/`anio` si elegiste la opción A). No es necesario declarar en ningún lado del código "esta es la opción A"; eso solo se indica en tu archivo [ENTREGA.md](ENTREGA.md).
