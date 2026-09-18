# Calificación automática (GitHub Pages)

Cada vez que subes un cambio a la rama `main`, un workflow de GitHub Actions (`.github/workflows/calificar.yml`) corre un calificador automático y publica un reporte en HTML en **GitHub Pages** de tu repositorio, con tu puntaje estimado y el detalle día por día.

## ¿Dónde veo mi reporte?

En tu repositorio: **Settings → Pages** te muestra la URL (normalmente `https://TU-USUARIO.github.io/TU-REPOSITORIO/`). También puedes verla en la pestaña **Actions**, en la ejecución más reciente del workflow "Calificar y publicar reporte".

> **Paso único que debes hacer tú:** GitHub Pages no se activa solo. La primera vez, entra a **Settings → Pages** de tu repositorio y en "Build and deployment" elige **Source: GitHub Actions**. Después de eso, cada push actualiza el sitio automáticamente.

## ¿Qué calcula el calificador?

Usa la misma rúbrica de [RUBRICA.md](RUBRICA.md) (20 puntos por día: 10 compila + 7 cumple la actividad + 3 commit correcto), pero de forma automática:

- **Compila (10 pts):** corre `javac` sobre la carpeta del día.
- **Cumple la actividad (7 pts):** corre tu `Main` y revisa **patrones**, no texto exacto — por ejemplo, que ya no aparezca la palabra `TODO` en la salida, que existan cierta cantidad de líneas de datos distintos, que la interfaz ya declare un método, que la excepción rechace el dato inválido, etc. El detalle exacto de cada día está comentado en [`scripts/calificar.py`](../scripts/calificar.py).
- **Commit correcto (3 pts):** busca en tu historial de Git un commit cuyo mensaje contenga el texto exacto pedido en [COMO-ENTREGAR.md](COMO-ENTREGAR.md) (ejemplo: `Dia 1: clase base`).

El reporte también muestra, como referencia visual ("contraste"), el mismo cálculo corrido sobre [`ejemplo-guia/`](../ejemplo-guia/) (la versión ya resuelta con el tema "Mascotas"), para que compares el patrón de tu código contra el del ejemplo.

## Por qué NO compara tu código letra por letra contra el ejemplo

Cada opción (A, B o C) usa nombres y datos distintos (`Material`/`Producto`/`Persona`, títulos de libros, precios, nombres de alumnos, etc.), y renombrar las clases genéricas es opcional (ver [OPCIONES.md](../OPCIONES.md)). Comparar texto exacto contra "Mascotas" no tendría sentido para una entrega sobre una tienda o una escuela. Por eso el calificador busca **patrones de comportamiento y de estructura del código** que son válidos sin importar los nombres que hayas elegido.

## Límites importantes

Esto es una **evaluación automática preliminar**, no la calificación final:

- Es una heurística: puede dar falsos positivos o negativos en casos poco comunes (por ejemplo, si cambias el texto de los mensajes de consola que ya venían en el `Main.java` original, o si tu solución es correcta pero muy distinta a lo esperado).
- No revisa estilo, comentarios, ni buenas prácticas más allá de lo que pide cada día.
- No sustituye la revisión de tu profesor/a, que es quien pone la calificación final.

Úsalo como una forma rápida de saber si vas por buen camino **antes** de tu entrega final, no como el resultado oficial.

## ¿Puedo correrlo en mi computadora antes de subir los cambios?

Sí. Necesitas Python 3 (ya viene instalado en macOS y Linux; en Windows instálalo desde [python.org](https://www.python.org/)) y el JDK 17 (ver [COMPILAR-Y-EJECUTAR.md](COMPILAR-Y-EJECUTAR.md)). Desde la raíz del proyecto:

```bash
python3 scripts/calificar.py
```

Esto genera `_site/index.html` (ábrelo con tu navegador) y `_site/reporte.json` con el detalle. Esa carpeta `_site/` es solo para pruebas locales; no se sube al repositorio (está en `.gitignore`).
