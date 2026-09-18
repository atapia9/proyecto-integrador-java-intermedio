# Día 5 — Menú integrador

**Objetivo:** construir un menú de consola que integre las clases de los 4 días anteriores.

## Qué entregar

- `Main.java` con un menú funcional (opciones 1-4) conectado a `GestorElementos`.
- El archivo [ENTREGA.md](../ENTREGA.md) lleno (datos generales, checklist y reflexión final).
- Un commit con el mensaje exacto: `Dia 5: menu integrador`

## Qué hacer

1. Todas las clases de los días 1 a 4 ya están copiadas y resueltas en esta carpeta; no necesitas modificarlas.
2. Abre `Main.java`. El menú (opciones 1 a 4, el `while` y el `Scanner`) ya está construido; tu trabajo es completar las 3 conexiones marcadas con `TODO`:
   - Opción 1 (agregar): llama a `gestor.agregar(new Elemento(nombre, detalle, cantidad));` dentro del `try`.
   - Opción 2 (listar): llama a `gestor.listar();`.
   - Opción 3 (buscar): llama a `gestor.buscarPorNombre(nombreBuscado)` y muestra el resultado (si regresa `null`, avisa que no se encontró).
3. Ejecuta el programa y prueba las 4 opciones al menos una vez.
4. Llena [ENTREGA.md](../ENTREGA.md) en la raíz del proyecto.

## Salida esperada en consola (ejemplo)

Con el tema "Mascotas" (ver `ejemplo-guia/dia5-integrador`), agregando a "Rocky" y después listando:

```
=== Dia 5: Menu integrador (Mascotas) ===
Perro -> Mascota: Firulais | Raza: Labrador | Edad: 3 anios
Gato -> Mascota: Michi | Raza: Siames | Edad: 2 anios
Firulais necesita paseos diarios y agua fresca.
Michi necesita su caja de arena limpia y rascador.

===== MENU =====
1) Agregar
2) Listar
3) Buscar por nombre
4) Salir
Elige una opcion: 1
Nombre: Rocky
Raza: Bulldog
Edad: 5
Mascota agregada correctamente.

===== MENU =====
1) Agregar
2) Listar
3) Buscar por nombre
4) Salir
Elige una opcion: 4
Hasta luego.
```

(El texto exacto que tú escribas al ejecutar `java Main` puede variar; lo importante es que las 4 opciones respondan correctamente.)

## Checklist

- [ ] Las 4 opciones del menú funcionan (agregar, listar, buscar, salir).
- [ ] El programa no se cierra solo (usa el `while` que ya viene armado) hasta elegir la opción 4.
- [ ] `ENTREGA.md` está lleno completamente.

## Si te atoras

Revisa la versión completa y resuelta en [ejemplo-guia/dia5-integrador/](../ejemplo-guia/dia5-integrador/).
