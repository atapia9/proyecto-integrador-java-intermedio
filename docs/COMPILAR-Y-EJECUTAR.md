# Cómo compilar y ejecutar tu código

## 1. Instalar el JDK 17

Necesitas el "Java Development Kit" versión 17 (LTS). No necesitas Maven, Gradle ni ningún IDE.

### Windows / macOS / Linux (recomendado para todos)

1. Entra a https://adoptium.net/ (Eclipse Temurin, es gratuito).
2. Descarga la versión **17 (LTS)** para tu sistema operativo.
3. Instala normalmente (siguiente, siguiente, finalizar).
4. Abre una terminal **nueva** (cmd, PowerShell o Terminal) y escribe:
   ```bash
   java -version
   javac -version
   ```
   Si ambos comandos muestran algo como `17.0.x`, ya quedó instalado correctamente.

### Alternativa macOS con Homebrew

```bash
brew install openjdk@17
```

### Alternativa Linux (Debian/Ubuntu)

```bash
sudo apt update
sudo apt install openjdk-17-jdk
```

## 2. Compilar y ejecutar un día

Todos los días se compilan y ejecutan igual. Desde la raíz del proyecto:

```bash
cd dia1-clase-base
javac -encoding UTF-8 *.java
java Main
```

Esto compila **todos** los archivos `.java` de la carpeta y luego ejecuta la clase `Main`.

> Usamos `-encoding UTF-8` para que la compilación sea igual en cualquier sistema operativo. Es opcional pero recomendado.

Para volver a la raíz del proyecto después de probar un día:
```bash
cd ..
```

## 3. Errores comunes de principiante y su solución

### "javac no se reconoce como un comando" / "command not found: javac"

**Causa:** el JDK no está instalado o no está en el PATH.
**Solución:** vuelve a instalar el JDK 17 (paso 1) y abre una terminal **nueva** (las terminales ya abiertas no ven el cambio).

### "error: class Main is public, should be declared in a file named Main.java"

**Causa:** copiaste el código de la clase `Main` dentro de un archivo con otro nombre.
**Solución:** el nombre del archivo debe ser exactamente igual al nombre de la clase pública, incluyendo mayúsculas: `Main.java` para `public class Main`.

### "error: cannot find symbol"

**Causa:** casi siempre es un error de escritura (nombre de variable, método o clase mal escrito) o falta compilar otro archivo que se usa.
**Solución:**
1. Revisa que el nombre esté escrito exactamente igual (Java distingue mayúsculas de minúsculas).
2. Asegúrate de compilar **todos** los `.java` de la carpeta a la vez: `javac *.java`, no uno por uno.

### "error: ';' expected" o "error: reached end of file while parsing"

**Causa:** te faltó un punto y coma `;` o una llave de cierre `}`.
**Solución:** revisa la línea que indica el error (y la línea anterior). Cuenta que cada `{` tenga su `}`.

### El programa compila pero no hace nada, o imprime cosas vacías

**Causa:** es normal en un esqueleto sin terminar: los métodos con `TODO` regresan valores vacíos o de relleno a propósito para que el proyecto compile.
**Solución:** completa los `TODO` indicados en el `INSTRUCCIONES.md` de esa carpeta.

### "Exception in thread main java.lang.NumberFormatException" (Día 5)

**Causa:** el menú esperaba un número y escribiste texto, o dejaste espacios de más.
**Solución:** escribe únicamente el número de la opción (ejemplo `1`) y presiona Enter.

### Los acentos se ven raros en la consola (Ã©, Ã±, etc.)

**Causa:** diferencia de codificación entre el archivo (UTF-8) y la consola de Windows.
**Solución:** ejecuta antes en la misma terminal:
```bash
chcp 65001
```
y vuelve a correr `java Main`. Esto no afecta tu calificación, es solo visual.

## 4. ¿Y si uso un IDE (VS Code, IntelliJ, Eclipse)?

Puedes usarlo si quieres, es opcional. Basta con que abras la carpeta del día correspondiente y ejecutes la clase `Main`. El proyecto **no** usa Maven ni Gradle, así que no busques (ni crees) un `pom.xml` ni un `build.gradle`.
