#!/usr/bin/env python3
# calificar.py
#
# Motor de calificacion automatica del Proyecto Integrador (Java Intermedio).
#
# Por que heuristicas y no un "diff" literal contra ejemplo-guia:
# los estudiantes pueden renombrar sus clases genericas (Elemento -> Material /
# Producto / Persona, ver OPCIONES.md) y usan datos propios, asi que el texto
# de salida NUNCA va a coincidir literalmente con el de "Mascotas". En vez de
# comparar texto, este script busca senales estructurales que no dependen del
# nombre de las clases ni del tema elegido:
#   - Los TODO sin resolver de las plantillas siempre imprimen o dejan la
#     palabra literal "TODO" en alguna salida/archivo; su ausencia es una
#     senal fuerte (e independiente del idioma/tema) de que se completo.
#   - Patrones estructurales (@Override, throw new, super(, firma de metodo
#     en una interfaz) se buscan en TODOS los .java de la carpeta, no en un
#     archivo con nombre fijo.
#   - El Dia 5 se prueba end-to-end con una entrada de Scanner fija.
# El mismo motor se corre contra ejemplo-guia (ya resuelto) para mostrar el
# "contraste" lado a lado en el reporte HTML.
import html
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DIAS = [
    {"num": 1, "carpeta": "dia1-clase-base", "commit": "Dia 1: clase base"},
    {"num": 2, "carpeta": "dia2-herencia", "commit": "Dia 2: herencia e interfaz"},
    {"num": 3, "carpeta": "dia3-colecciones", "commit": "Dia 3: colecciones"},
    {"num": 4, "carpeta": "dia4-excepciones", "commit": "Dia 4: excepciones"},
    {"num": 5, "carpeta": "dia5-integrador", "commit": "Dia 5: menu integrador"},
]

TIMEOUT_COMPILAR = 30
TIMEOUT_EJECUTAR = 10


def leer_fuentes(carpeta):
    """Regresa {nombre_archivo: contenido} de todos los .java en la carpeta (no recursivo)."""
    fuentes = {}
    if not os.path.isdir(carpeta):
        return fuentes
    for nombre in sorted(os.listdir(carpeta)):
        if nombre.endswith(".java"):
            with open(os.path.join(carpeta, nombre), "r", encoding="utf-8", errors="replace") as f:
                fuentes[nombre] = f.read()
    return fuentes


def quitar_comentarios(codigo):
    """Elimina comentarios // y /* */ para no confundir un TODO comentado con codigo real."""
    sin_bloque = re.sub(r"/\*.*?\*/", " ", codigo, flags=re.DOTALL)
    sin_linea = re.sub(r"//.*", "", sin_bloque)
    return sin_linea


def compilar(carpeta, out_dir):
    """Compila todos los .java de la carpeta. Regresa (exito, log)."""
    if not os.path.isdir(carpeta):
        return False, "La carpeta no existe."
    archivos = [f for f in sorted(os.listdir(carpeta)) if f.endswith(".java")]
    if not archivos:
        return False, "No hay archivos .java en la carpeta."
    os.makedirs(out_dir, exist_ok=True)
    cmd = ["javac", "-encoding", "UTF-8", "-d", out_dir] + archivos
    try:
        resultado = subprocess.run(
            cmd, cwd=carpeta, capture_output=True, text=True, timeout=TIMEOUT_COMPILAR
        )
    except subprocess.TimeoutExpired:
        return False, "javac tardo demasiado (timeout)."
    if resultado.returncode != 0:
        return False, resultado.stderr.strip()[-4000:]
    return True, "OK"


def ejecutar_main(class_dir, entrada=""):
    """Ejecuta la clase Main con la entrada dada por stdin. Regresa (stdout, ok)."""
    try:
        resultado = subprocess.run(
            ["java", "-cp", class_dir, "Main"],
            input=entrada,
            capture_output=True,
            text=True,
            timeout=TIMEOUT_EJECUTAR,
        )
    except subprocess.TimeoutExpired:
        return "(el programa no termino a tiempo, probablemente se quedo esperando datos de Scanner)", False
    return (resultado.stdout or "") + (("\n[stderr]\n" + resultado.stderr) if resultado.returncode != 0 else ""), True


def lineas_no_vacias(texto):
    return [l for l in texto.splitlines() if l.strip() != ""]


def lineas_de_datos(texto):
    """Como lineas_no_vacias pero descarta encabezados tipo '=== Dia N: ... ==='."""
    return [l for l in lineas_no_vacias(texto) if not re.match(r"^\s*={2,}", l)]


# ---------------------------------------------------------------------------
# Heuristicas de "cumple la actividad" (7 pts por dia). Cada funcion regresa
# (puntos_obtenidos, puntos_max, lista_de_strings_con_detalle).
# ---------------------------------------------------------------------------

def revisar_dia1(fuentes, salida):
    detalle = []
    pts = 0.0
    if "TODO" not in salida:
        pts += 4
        detalle.append(("ok", "La salida ya no contiene texto 'TODO' (getters/toString completos)."))
    else:
        detalle.append(("fail", "La salida todavia contiene 'TODO': faltan getters, constructor o toString()."))

    lineas = lineas_de_datos(salida)
    if len(lineas) >= 3 and len(set(lineas)) >= 2:
        pts += 3
        detalle.append(("ok", "Se imprimen al menos 3 objetos y no son todos identicos."))
    else:
        detalle.append(("fail", "Se esperaban al menos 3 lineas de salida con datos distintos entre si."))
    return pts, 7, detalle


def revisar_dia2(fuentes, salida):
    detalle = []
    pts = 0.0
    todo_junto = "\n".join(quitar_comentarios(c) for c in fuentes.values())

    # 1) La interfaz debe declarar al menos un metodo (firma terminada en ';')
    interfaz_ok = False
    for contenido in fuentes.values():
        sin_comentarios = quitar_comentarios(contenido)
        if re.search(r"\binterface\s+\w+", sin_comentarios):
            cuerpo = sin_comentarios.split("{", 1)[-1]
            if re.search(r"[A-Za-z_][\w<>\[\],\s]*\s+\w+\s*\([^;{}]*\)\s*;", cuerpo):
                interfaz_ok = True
                break
    if interfaz_ok:
        pts += 2
        detalle.append(("ok", "La interfaz ya declara un metodo (ya no esta vacia)."))
    else:
        detalle.append(("fail", "No se encontro un metodo declarado dentro de la interfaz."))

    # 2) @Override deberia aparecer al menos 5 veces: la base (Elemento.toString) ya trae
    # 1, y las 2 subclases ya traen @Override en el mostrarInfo() sin terminar (2 mas) desde
    # el esqueleto; el trabajo real del dia agrega 2 mas (una por subclase, del metodo de
    # la interfaz), asi que el punto de corte es 5, no 3 (3 es el punto de partida sin hacer nada).
    overrides = len(re.findall(r"@Override", todo_junto))
    if overrides >= 5:
        pts += 2
        detalle.append(("ok", f"Se encontraron {overrides} usos de @Override."))
    else:
        detalle.append(("fail", f"Solo se encontraron {overrides} usos de @Override (se esperaban 5 o mas)."))

    # 3) La salida debe tener al menos 2 lineas no vacias y distintas entre si
    lineas = lineas_de_datos(salida)
    if len(lineas) >= 2 and len(set(lineas)) >= 2 and "TODO" not in salida:
        pts += 3
        detalle.append(("ok", "mostrarInfo() de ambas subclases produce salida distinta."))
    else:
        detalle.append(("fail", "La salida de mostrarInfo() esta vacia, repetida o incompleta."))
    return pts, 7, detalle


def revisar_dia3(fuentes, salida):
    detalle = []
    pts = 0.0
    if "TODO" not in salida:
        pts += 2
        detalle.append(("ok", "listar() y buscarPorNombre() ya no dejan texto 'TODO'."))
    else:
        detalle.append(("fail", "Todavia aparece 'TODO' en la salida (listar o buscarPorNombre sin terminar)."))

    if "Lista completa:" in salida:
        seccion = salida.split("Lista completa:", 1)[1]
        # El corte de la seccion de listado termina donde empieza el resultado de la
        # busqueda (marcador "Buscando", o directamente la linea de resultado si el
        # Main no imprime un marcador de "Buscando", como en la plantilla generica).
        corte = re.search(r"Buscando|Encontrad[oa]:|No se encontro", seccion)
        resto = seccion[: corte.start()] if corte else seccion
        lineas_lista = lineas_no_vacias(resto)
    else:
        lineas_lista = []
    if len(lineas_lista) >= 3:
        pts += 3
        detalle.append(("ok", f"listar() imprime {len(lineas_lista)} elementos."))
    else:
        detalle.append(("fail", f"listar() solo imprimio {len(lineas_lista)} elemento(s); se esperaban 3 o mas."))

    if re.search(r"Encontrad[oa]:", salida):
        pts += 2
        detalle.append(("ok", "buscarPorNombre() encontro el elemento esperado."))
    else:
        detalle.append(("fail", "buscarPorNombre() no encontro el elemento que si existe en la lista."))
    return pts, 7, detalle


def revisar_dia4(fuentes, salida):
    detalle = []
    pts = 0.0
    if "Este mensaje no se deberia imprimir" not in salida:
        pts += 4
        detalle.append(("ok", "El dato invalido fue rechazado (la excepcion se lanzo y se capturo)."))
    else:
        detalle.append(("fail", "El dato invalido NO fue rechazado: falta la validacion en agregar()."))

    if "Lista final:" in salida:
        resto = salida.split("Lista final:", 1)[1]
        lineas_final = lineas_no_vacias(resto)
    else:
        lineas_final = []
    if len(lineas_final) == 1:
        pts += 2
        detalle.append(("ok", "La lista final contiene solo el objeto valido (el invalido no se agrego)."))
    else:
        detalle.append(("fail", f"La lista final tiene {len(lineas_final)} elemento(s); se esperaba exactamente 1."))

    excepcion_ok = False
    for contenido in fuentes.values():
        sin_comentarios = quitar_comentarios(contenido)
        if re.search(r"extends\s+Exception\b", sin_comentarios) and re.search(r"super\s*\(", sin_comentarios):
            excepcion_ok = True
            break
    if excepcion_ok:
        pts += 1
        detalle.append(("ok", "La excepcion propia guarda el mensaje con super(...)."))
    else:
        detalle.append(("fail", "No se encontro una excepcion (extends Exception) que use super(...)."))
    return pts, 7, detalle


def revisar_dia5(fuentes, salida, main_fuente):
    detalle = []
    pts = 0.0
    marcadores = [
        "TODO: falta llamar a gestor.agregar()",
        "TODO: falta llamar a gestor.listar()",
        "TODO: falta llamar a gestor.buscarPorNombre()",
    ]
    resueltos = sum(1 for m in marcadores if m not in (main_fuente or "") and m not in salida)
    pts += resueltos  # 1 pt por cada conexion resuelta (max 3)
    detalle.append(("ok" if resueltos == 3 else "fail",
                     f"{resueltos} de 3 conexiones del menu con GestorElementos ya estan hechas."))

    apariciones = salida.count("ClaveDePrueba123")
    if apariciones >= 2:
        pts += 3
        detalle.append(("ok", "El dato de prueba viaja correctamente por agregar -> listar -> buscar."))
    elif apariciones == 1:
        pts += 1.5
        detalle.append(("fail", "El dato de prueba solo aparecio una vez (falla listar o buscar)."))
    else:
        detalle.append(("fail", "El dato de prueba no aparecio en la salida (falla agregar)."))

    entrega_path = os.path.join(REPO_ROOT, "ENTREGA.md")
    entrega_llena = False
    if os.path.isfile(entrega_path):
        with open(entrega_path, "r", encoding="utf-8", errors="replace") as f:
            texto = f.read()
        m = re.search(r"Nombre completo:\**[ \t]*(.*)", texto)
        if m and m.group(1).strip():
            entrega_llena = True
    if entrega_llena:
        pts += 1
        detalle.append(("ok", "ENTREGA.md tiene el nombre completo lleno."))
    else:
        detalle.append(("fail", "ENTREGA.md no tiene llenado el campo 'Nombre completo'."))
    return pts, 7, detalle


ENTRADA_DIA5 = "1\nClaveDePrueba123\nDetalleDePrueba\n42\n2\n3\nClaveDePrueba123\n4\n"

REVISORES = {1: revisar_dia1, 2: revisar_dia2, 3: revisar_dia3, 4: revisar_dia4}


def commit_existe(mensaje_requerido):
    try:
        resultado = subprocess.run(
            ["git", "log", "--all", "--format=%s"],
            cwd=REPO_ROOT, capture_output=True, text=True, timeout=15,
        )
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False
    if resultado.returncode != 0:
        return False
    mensajes = resultado.stdout.splitlines()
    return any(mensaje_requerido in m for m in mensajes)


def calificar_carpeta(carpeta_abs, dia_num, con_commit, commit_msg, build_root):
    resultado = {
        "compila": False, "compila_log": "", "pts_compila": 0,
        "pts_actividad": 0, "max_actividad": 7, "detalle_actividad": [],
        "pts_commit": None, "max_commit": 3 if con_commit else 0,
        "salida": "",
    }
    out_dir = os.path.join(build_root, f"dia{dia_num}")
    ok, log = compilar(carpeta_abs, out_dir)
    resultado["compila"] = ok
    resultado["compila_log"] = log
    if not ok:
        resultado["detalle_actividad"] = [("fail", "No se evalua la actividad porque el codigo no compila.")]
        if con_commit:
            resultado["pts_commit"] = 3 if commit_existe(commit_msg) else 0
        return resultado

    resultado["pts_compila"] = 10
    fuentes = leer_fuentes(carpeta_abs)
    entrada = ENTRADA_DIA5 if dia_num == 5 else ""
    salida, corrio = ejecutar_main(out_dir, entrada)
    resultado["salida"] = salida

    if dia_num == 5:
        main_fuente = fuentes.get("Main.java", "")
        pts, maxp, detalle = revisar_dia5(fuentes, salida, main_fuente)
    else:
        pts, maxp, detalle = REVISORES[dia_num](fuentes, salida)
    resultado["pts_actividad"] = pts
    resultado["max_actividad"] = maxp
    resultado["detalle_actividad"] = detalle

    if con_commit:
        resultado["pts_commit"] = 3 if commit_existe(commit_msg) else 0
    return resultado


def generar_reporte():
    build_root = os.path.join(REPO_ROOT, "_build_calificar")
    ahora = datetime.now(timezone.utc)
    reporte = {
        "entrega": [], "referencia": [],
        "generado": ahora.isoformat(),
        "generado_legible": ahora.strftime("%Y-%m-%d %H:%M UTC"),
    }

    total_entrega = 0
    total_max_entrega = 0
    for dia in DIAS:
        carpeta = os.path.join(REPO_ROOT, dia["carpeta"])
        r = calificar_carpeta(carpeta, dia["num"], True, dia["commit"], os.path.join(build_root, "entrega"))
        subtotal = r["pts_compila"] + r["pts_actividad"] + (r["pts_commit"] or 0)
        r["dia"] = dia["num"]
        r["carpeta"] = dia["carpeta"]
        r["subtotal"] = subtotal
        reporte["entrega"].append(r)
        total_entrega += subtotal
        total_max_entrega += 20

    total_ref = 0
    total_max_ref = 0
    for dia in DIAS:
        carpeta = os.path.join(REPO_ROOT, "ejemplo-guia", dia["carpeta"])
        r = calificar_carpeta(carpeta, dia["num"], False, dia["commit"], os.path.join(build_root, "referencia"))
        subtotal = r["pts_compila"] + r["pts_actividad"]
        r["dia"] = dia["num"]
        r["carpeta"] = "ejemplo-guia/" + dia["carpeta"]
        r["subtotal"] = subtotal
        reporte["referencia"].append(r)
        total_ref += subtotal
        total_max_ref += 17

    reporte["total_entrega"] = total_entrega
    reporte["total_max_entrega"] = total_max_entrega
    reporte["total_referencia"] = total_ref
    reporte["total_max_referencia"] = total_max_ref
    reporte["aprobado"] = total_entrega >= 60
    return reporte


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

def badge(ok):
    return '<span class="badge ok">&#10003;</span>' if ok else '<span class="badge fail">&#10007;</span>'


def fila_detalle(detalle):
    items = "".join(
        f'<li class="{"ok" if tipo == "ok" else "fail"}">{html.escape(texto)}</li>'
        for tipo, texto in detalle
    )
    return f"<ul class='detalle'>{items}</ul>"


def tabla_dias(filas, con_commit):
    encabezado_commit = "<th>Commit</th>" if con_commit else ""
    out = ["<div class='tabla-scroll'>",
           f"<table class='tabla-dias'><thead><tr><th>Dia</th><th>Compila</th>"
           f"<th>Actividad</th>{encabezado_commit}<th>Total</th></tr></thead><tbody>"]
    for r in filas:
        commit_celda = ""
        if con_commit:
            if r["pts_commit"] is None:
                commit_celda = "<td class='centro'>N/A</td>"
            else:
                commit_celda = f"<td class='centro'>{badge(r['pts_commit'] == 3)} {r['pts_commit']}/3</td>"
        max_total = 20 if con_commit else 17
        out.append(
            f"<tr><td>Dia {r['dia']}<br><span class='carpeta'>{html.escape(r['carpeta'])}</span></td>"
            f"<td class='centro'>{badge(r['compila'])} {r['pts_compila']}/10</td>"
            f"<td class='centro'>{r['pts_actividad']:.1f}/{r['max_actividad']}</td>"
            f"{commit_celda}"
            f"<td class='centro subtotal'>{r['subtotal']:.1f}/{max_total}</td></tr>"
        )
        detalle_extra = r["detalle_actividad"]
        if not r["compila"]:
            detalle_extra = [("fail", "No compila: " + r["compila_log"].splitlines()[-1] if r["compila_log"] else "No compila.")]
        colspan = 5 if con_commit else 4
        out.append(f"<tr class='fila-detalle'><td colspan='{colspan}'>{fila_detalle(detalle_extra)}</td></tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


PLANTILLA_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Calificacion automatica - Proyecto Integrador Java Intermedio</title>
<style>
  :root {{
    --bg: #f7f8fa; --card: #ffffff; --text: #1a1d23; --muted: #64707d;
    --border: #e3e7ec; --ok: #1a7f37; --ok-bg: #e6f6ea; --fail: #c4302b;
    --fail-bg: #fdecea; --accent: #2f6fed; --accent-bg: #eaf1ff;
  }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --bg: #0f1216; --card: #171b21; --text: #e7eaee; --muted: #98a3af;
      --border: #2a2f37; --ok: #4bd07a; --ok-bg: #12301e; --fail: #ff6b64;
      --fail-bg: #3a1414; --accent: #6ea2ff; --accent-bg: #142238;
    }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; padding: 24px 16px 64px; background: var(--bg); color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}
  .contenedor {{ max-width: 920px; margin: 0 auto; }}
  h1 {{ font-size: 1.5rem; margin: 0 0 4px; }}
  .subtitulo {{ color: var(--muted); font-size: 0.9rem; margin-bottom: 24px; }}
  .tarjeta {{
    background: var(--card); border: 1px solid var(--border); border-radius: 12px;
    padding: 20px; margin-bottom: 20px;
  }}
  .resumen {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; }}
  .puntaje-grande {{ font-size: 2.6rem; font-weight: 700; line-height: 1; }}
  .puntaje-grande.aprobado {{ color: var(--ok); }}
  .puntaje-grande.reprobado {{ color: var(--fail); }}
  .etiqueta-resultado {{
    display: inline-block; padding: 4px 12px; border-radius: 999px; font-weight: 600;
    font-size: 0.85rem;
  }}
  .etiqueta-resultado.aprobado {{ background: var(--ok-bg); color: var(--ok); }}
  .etiqueta-resultado.reprobado {{ background: var(--fail-bg); color: var(--fail); }}
  .tabla-scroll {{ overflow-x: auto; margin: 0 -20px; padding: 0 20px; }}
  table.tabla-dias {{ width: 100%; min-width: 360px; border-collapse: collapse; font-size: 0.82rem; }}
  table.tabla-dias th {{
    text-align: left; padding: 6px 6px; border-bottom: 2px solid var(--border);
    color: var(--muted); font-weight: 600; white-space: nowrap;
  }}
  table.tabla-dias td {{ padding: 6px 6px; border-bottom: 1px solid var(--border); vertical-align: top; }}
  td.centro {{ text-align: center; white-space: nowrap; }}
  td.subtotal {{ font-weight: 700; }}
  .carpeta {{ color: var(--muted); font-size: 0.78rem; font-family: monospace; }}
  .badge {{
    display: inline-block; font-size: 0.7rem; font-weight: 700; padding: 1px 6px;
    border-radius: 4px; margin-right: 4px;
  }}
  .badge.ok {{ background: var(--ok-bg); color: var(--ok); }}
  .badge.fail {{ background: var(--fail-bg); color: var(--fail); }}
  tr.fila-detalle td {{ border-bottom: 1px solid var(--border); padding-top: 0; }}
  ul.detalle {{ margin: 0; padding-left: 18px; font-size: 0.82rem; color: var(--muted); }}
  ul.detalle li.ok::marker {{ color: var(--ok); }}
  ul.detalle li.fail::marker {{ color: var(--fail); }}
  .nota {{
    background: var(--accent-bg); color: var(--accent); border-radius: 8px;
    padding: 12px 14px; font-size: 0.85rem; margin-top: 8px;
  }}
  footer {{ color: var(--muted); font-size: 0.78rem; text-align: center; margin-top: 32px; }}
  h2 {{ font-size: 1.1rem; margin-top: 0; }}
</style>
</head>
<body>
<div class="contenedor">
  <h1>Calificacion automatica del Proyecto Integrador</h1>
  <div class="subtitulo">Generado el {generado} &middot; commit <code>{commit_sha}</code></div>

  <div class="tarjeta resumen">
    <div class="puntaje-grande {clase_resultado}">{total_entrega:.1f}<span style="font-size:1.4rem;color:var(--muted);">/100</span></div>
    <div>
      <div class="etiqueta-resultado {clase_resultado}">{texto_resultado}</div>
      <div class="subtitulo" style="margin-top:8px;">
        Referencia (ejemplo-guia): {total_referencia:.1f}/{total_max_referencia} puntos posibles de codigo
        (no incluye el criterio de commit, que no aplica a una carpeta de referencia).
      </div>
    </div>
  </div>

  <div class="tarjeta">
    <h2>Tu entrega</h2>
    {tabla_entrega}
  </div>

  <div class="tarjeta">
    <h2>Referencia (ejemplo-guia, tema "Mascotas")</h2>
    {tabla_referencia}
  </div>

  <div class="nota">
    Esta es una <strong>evaluacion automatica preliminar</strong> basada en heuristicas
    (compila, patrones estructurales del codigo y comportamiento al ejecutar el programa).
    No reemplaza la revision de tu profesor/a; usala para saber en que estas parado/a antes
    de la entrega final. Ver <a href="https://github.com/{repo}/blob/main/docs/CALIFICACION-AUTOMATICA.md" style="color:inherit;">como funciona</a>.
  </div>

  <footer>Proyecto Integrador &mdash; Java Intermedio &middot; REDEC-UNAM / FES Cuautitlan</footer>
</div>
</body>
</html>
"""


def construir_html(reporte, repo, commit_sha):
    clase_resultado = "aprobado" if reporte["aprobado"] else "reprobado"
    texto_resultado = "APROBADO" if reporte["aprobado"] else "NO APROBADO (minimo 60)"
    return PLANTILLA_HTML.format(
        generado=reporte["generado_legible"],
        commit_sha=commit_sha[:8],
        total_entrega=reporte["total_entrega"],
        total_referencia=reporte["total_referencia"],
        total_max_referencia=reporte["total_max_referencia"],
        clase_resultado=clase_resultado,
        texto_resultado=texto_resultado,
        tabla_entrega=tabla_dias(reporte["entrega"], con_commit=True),
        tabla_referencia=tabla_dias(reporte["referencia"], con_commit=False),
        repo=repo,
    )


def obtener_commit_sha():
    try:
        r = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO_ROOT,
                            capture_output=True, text=True, timeout=10)
        return r.stdout.strip() or "desconocido"
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return "desconocido"


def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "atapia9/proyecto-integrador-java-intermedio")
    reporte = generar_reporte()
    commit_sha = obtener_commit_sha()

    out_dir = os.environ.get("SITE_DIR", os.path.join(REPO_ROOT, "_site"))
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(construir_html(reporte, repo, commit_sha))
    with open(os.path.join(out_dir, "reporte.json"), "w", encoding="utf-8") as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)

    print(f"Puntaje total (tu entrega): {reporte['total_entrega']:.1f}/{reporte['total_max_entrega']}")
    print(f"Puntaje de referencia (ejemplo-guia): {reporte['total_referencia']:.1f}/{reporte['total_max_referencia']}")
    print(f"Resultado: {'APROBADO' if reporte['aprobado'] else 'NO APROBADO'}")
    print(f"Reporte HTML escrito en: {os.path.join(out_dir, 'index.html')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
