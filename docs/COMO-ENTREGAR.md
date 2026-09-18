# Cómo entregar tu proyecto

Tienes 2 formas de entregar. Elige la que te resulte más cómoda; **ambas son válidas y tienen el mismo valor**.

## Mensajes de commit exactos

Usa **exactamente** estos mensajes al terminar cada día (la rúbrica revisa que el mensaje sea correcto):

| Día | Mensaje de commit |
|---|---|
| 1 | `Dia 1: clase base` |
| 2 | `Dia 2: herencia e interfaz` |
| 3 | `Dia 3: colecciones` |
| 4 | `Dia 4: excepciones` |
| 5 | `Dia 5: menu integrador` |

---

## Ruta 1: Git en terminal

Usa esta ruta si ya tienes Git instalado y sabes abrir una terminal.

1. Clona tu repositorio (solo la primera vez):
   ```bash
   git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
   cd TU-REPOSITORIO
   ```
2. Edita los archivos del día correspondiente (por ejemplo, `dia1-clase-base/Elemento.java`).
3. Guarda tus cambios en Git:
   ```bash
   git add dia1-clase-base
   git commit -m "Dia 1: clase base"
   git push
   ```
4. Repite los pasos 2 y 3 para cada día, cambiando la carpeta y el mensaje de commit según la tabla de arriba.

> Tip: puedes usar `git add .` si ya revisaste con `git status` que solo se están agregando los archivos del proyecto.

---

## Ruta 2: Solo navegador (sin instalar nada)

Usa esta ruta si no tienes Git instalado o no te sientes cómodo con la terminal. Todo se hace desde github.com.

1. Entra a tu repositorio en github.com.
2. Entra a la carpeta del día que vas a editar (ejemplo: `dia1-clase-base`).
3. Da clic en el archivo que vas a modificar (ejemplo: `Elemento.java`).
4. Da clic en el ícono de lápiz ("Edit this file") en la esquina superior derecha.
5. Modifica el código directamente en el editor de GitHub.
6. Baja hasta el final de la página, en "Commit changes":
   - En el primer cuadro de texto, escribe **exactamente** el mensaje de commit de la tabla de arriba (ejemplo: `Dia 1: clase base`).
   - Deja seleccionada la opción "Commit directly to the main branch".
   - Da clic en el botón verde "Commit changes".
7. Repite para cada archivo que necesites modificar ese día.
8. Repite todo el proceso para los días 2 a 5.

### Subir un archivo nuevo desde el navegador

Si necesitas agregar un archivo nuevo (por ejemplo, una clase nueva):

1. Entra a la carpeta donde debe ir el archivo.
2. Da clic en "Add file" → "Create new file".
3. Escribe el nombre del archivo (ejemplo: `ElementoTipoA.java`).
4. Pega o escribe el contenido.
5. Baja y haz el commit con el mensaje correcto, igual que en el paso 6 de arriba.

---

## Cómo confirmar que tu entrega quedó bien

Después de cada commit (por cualquiera de las 2 rutas), revisa la pestaña **"Actions"** de tu repositorio en GitHub. Debe aparecer una palomita verde ✅ junto a tu commit. Si aparece una X roja ❌, entra al detalle para ver qué carpeta falló y corrígela (ver [COMPILAR-Y-EJECUTAR.md](COMPILAR-Y-EJECUTAR.md)).
