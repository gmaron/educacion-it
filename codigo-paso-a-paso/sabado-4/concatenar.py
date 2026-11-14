"""Junta todos los archivos del proyecto en un solo proyecto.txt."""

from pathlib import Path

RAIZ = Path(__file__).resolve().parent
SALIDA = RAIZ / "proyecto.txt"
CARPETAS_SALTEADAS = {".venv", "__pycache__", ".pytest_cache", ".git"}
ARCHIVOS_SALTEADOS = {SALIDA.name, Path(__file__).name}


def archivos_del_proyecto():
    """Devuelve las rutas de los archivos a juntar, ordenadas."""
    rutas = []
    for ruta in sorted(RAIZ.rglob("*")):
        relativa = ruta.relative_to(RAIZ)
        if any(parte in CARPETAS_SALTEADAS for parte in relativa.parts):
            continue
        if ruta.is_file() and relativa.as_posix() not in ARCHIVOS_SALTEADOS:
            rutas.append(ruta)
    return rutas


def main():
    """Escribe proyecto.txt e imprime el resumen."""
    partes = []
    for ruta in archivos_del_proyecto():
        try:
            contenido = ruta.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue  # binario: no sirve como texto
        partes.append(f"=== {ruta.relative_to(RAIZ).as_posix()} ===\n")
        if not contenido.endswith("\n"):
            contenido += "\n"
        partes.append(contenido)
        partes.append("\n")

    texto = "".join(partes)
    SALIDA.write_text(texto, encoding="utf-8")

    archivos = len(partes) // 3
    caracteres = len(texto)
    print(f"Archivos: {archivos}")
    print(f"Caracteres: {caracteres}")
    print(f"Tokens estimados: {caracteres // 4}")


if __name__ == "__main__":
    main()
