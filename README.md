# Proyecto Integrador – Java Intermedio

Bienvenido/a al Proyecto Integrador del curso **Java Intermedio** (REDEC-UNAM / FES Cuautitlán, educación continua).

Este proyecto se entrega en **5 días de trabajo**, uno por concepto. Cada día tiene su propia carpeta con un esqueleto de código que **ya compila desde el primer momento**: tu trabajo es completar los `TODO` que encontrarás comentados dentro del código.

> No necesitas Maven, Gradle ni ningún IDE en especial. Con el JDK 17 y los comandos `javac`/`java` es suficiente. Revisa [docs/COMPILAR-Y-EJECUTAR.md](docs/COMPILAR-Y-EJECUTAR.md) si nunca lo has hecho.

## Cómo usar esta plantilla

1. Usa el botón verde **"Use this template"** de GitHub (o el enlace que te dé tu profesor/a) para crear tu propio repositorio a partir de esta plantilla.
2. Entra a tu repositorio y elige cómo vas a trabajar: con Git en terminal o solo desde el navegador (ver [docs/COMO-ENTREGAR.md](docs/COMO-ENTREGAR.md)).
3. Elige **una sola opción** de tema para tu proyecto (ver siguiente sección).
4. Sigue el cronograma día por día. Cada carpeta `diaN-...` tiene su propio archivo `INSTRUCCIONES.md`.
5. Llena el archivo [ENTREGA.md](ENTREGA.md) al terminar el día 5.

## Cómo elegir tu opción

Debes elegir **una sola opción** (A, B o C) y usarla durante los 5 días. El detalle completo está en [OPCIONES.md](OPCIONES.md):

| Opción | Tema | Clase base | Subclases | Interfaz |
|---|---|---|---|---|
| A | Biblioteca | `Material` | `Libro`, `Revista` | `Prestable` |
| B | Tienda | `Producto` | `Alimento`, `Electronico` | `Vendible` |
| C | Escuela | `Persona` | `Alumno`, `Profesor` | `Evaluable` |

No hay una opción "mejor" que otra: elige la que te resulte más fácil de imaginar con datos reales.

Si en algún momento te atoras, en la carpeta [ejemplo-guia/](ejemplo-guia/) encontrarás el proyecto **completo y resuelto** con el tema "Mascotas" (`Mascota`, `Perro`, `Gato`, `Cuidable`). Puedes usarlo como guía y adaptar los nombres a tu opción.

## Cronograma (5 días)

| Día | Carpeta | Tema | Instrucciones |
|---|---|---|---|
| 1 | [dia1-clase-base/](dia1-clase-base/) | Clase, atributos, constructor, getters/setters | [INSTRUCCIONES.md](dia1-clase-base/INSTRUCCIONES.md) |
| 2 | [dia2-herencia/](dia2-herencia/) | Herencia e interfaces | [INSTRUCCIONES.md](dia2-herencia/INSTRUCCIONES.md) |
| 3 | [dia3-colecciones/](dia3-colecciones/) | `ArrayList` (agregar, listar, buscar) | [INSTRUCCIONES.md](dia3-colecciones/INSTRUCCIONES.md) |
| 4 | [dia4-excepciones/](dia4-excepciones/) | Excepciones propias (`try`/`catch`) | [INSTRUCCIONES.md](dia4-excepciones/INSTRUCCIONES.md) |
| 5 | [dia5-integrador/](dia5-integrador/) | Menú con `Scanner` que integra todo | [INSTRUCCIONES.md](dia5-integrador/INSTRUCCIONES.md) |

Al terminar cada día, haz un commit con el mensaje exacto indicado en [docs/COMO-ENTREGAR.md](docs/COMO-ENTREGAR.md).

## Checklist general por día

- [ ] **Día 1**: `Elemento` con 3 atributos, constructor, getters/setters y `toString()`. Commit: `Dia 1: clase base`
- [ ] **Día 2**: 2 subclases con `mostrarInfo()` sobrescrito + 1 interfaz implementada por ambas. Commit: `Dia 2: herencia e interfaz`
- [ ] **Día 3**: `ArrayList` con al menos 3 objetos, `listar()` y `buscarPorNombre()`. Commit: `Dia 3: colecciones`
- [ ] **Día 4**: excepción propia lanzada y capturada con `try`/`catch`. Commit: `Dia 4: excepciones`
- [ ] **Día 5**: menú de consola funcional + [ENTREGA.md](ENTREGA.md) lleno. Commit: `Dia 5: menu integrador`

## Rúbrica (resumen)

100 puntos totales, 20 por día (10 compila + 7 cumple la actividad + 3 commit correcto). Aprobación: 60 puntos. Detalle completo en [docs/RUBRICA.md](docs/RUBRICA.md).

## Calificación automática (feedback inmediato)

Cada push a `main` corre un calificador automático y publica un reporte HTML en GitHub Pages con tu puntaje estimado día por día, contrastado contra la referencia de [ejemplo-guia/](ejemplo-guia/). **Requiere un paso único de tu parte**: activar Pages en Settings → Pages → Source: GitHub Actions. Detalle completo (qué revisa, sus límites, cómo correrlo en tu máquina) en [docs/CALIFICACION-AUTOMATICA.md](docs/CALIFICACION-AUTOMATICA.md). Esto es una evaluación preliminar automática; no sustituye la calificación de tu profesor/a.

## Estructura del repositorio

```
proyecto-integrador-java-intermedio/
├── README.md
├── ENTREGA.md
├── OPCIONES.md
├── docs/
│   ├── COMO-ENTREGAR.md
│   ├── COMPILAR-Y-EJECUTAR.md
│   ├── RUBRICA.md
│   └── CALIFICACION-AUTOMATICA.md
├── scripts/
│   └── calificar.py
├── dia1-clase-base/
├── dia2-herencia/
├── dia3-colecciones/
├── dia4-excepciones/
├── dia5-integrador/
└── ejemplo-guia/        (proyecto completo y resuelto, tema "Mascotas")
```

## Si te atoras

1. Lee la sección "Si te atoras" del `INSTRUCCIONES.md` de tu día actual.
2. Compara tu código con la carpeta equivalente en [ejemplo-guia/](ejemplo-guia/).
3. Revisa [docs/COMPILAR-Y-EJECUTAR.md](docs/COMPILAR-Y-EJECUTAR.md) si el problema es al compilar.
4. Pregunta a tu profesor/a o en el foro del curso. **Entregar algo incompleto pero que compile vale más que no entregar nada.**
