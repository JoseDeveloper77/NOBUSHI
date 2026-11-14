#!/usr/bin/env python3
"""Regenera temas/lista.json a partir de los audios que haya en la carpeta temas/.

Uso (desde la carpeta del proyecto):   python3 actualizar-lista.py

- Mantiene el orden que ya tenía lista.json y añade al final los temas nuevos.
- Quita de la lista los archivos que ya no existen.
- Apunta el tamaño de cada archivo ("v"): si sustituyes un audio manteniendo el nombre,
  la app lo detecta como versión nueva y se actualiza en todos los móviles.
- Cambia los nombres con tildes al formato estándar (los archivos creados en Mac a veces
  usan otro formato y dan problemas en los enlaces).
"""
import json, os, sys, unicodedata

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temas")
LISTA = os.path.join(DIR, "lista.json")
EXT = (".mp3", ".m4a", ".wav", ".ogg", ".opus", ".flac", ".aac")


def main():
    if not os.path.isdir(DIR):
        sys.exit("No encuentro la carpeta temas/")

    # normalizar nombres (NFC)
    for n in os.listdir(DIR):
        f = unicodedata.normalize("NFC", n)
        if f != n:
            os.rename(os.path.join(DIR, n), os.path.join(DIR, f))
            print("Renombrado:", f)

    files = sorted(n for n in os.listdir(DIR) if n.lower().endswith(EXT))
    try:
        old = json.load(open(LISTA, encoding="utf-8"))
    except (OSError, ValueError):
        old = []

    names = {e["file"]: e.get("name") for e in old if isinstance(e, dict) and e.get("file")}
    order = [e["file"] for e in old if isinstance(e, dict) and e.get("file") in files]
    order += [f for f in files if f not in order]

    out = [{"file": f, "name": names.get(f) or os.path.splitext(f)[0],
            "v": os.path.getsize(os.path.join(DIR, f))} for f in order]
    with open(LISTA, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("%d temas en lista.json:" % len(out))
    for i, e in enumerate(out, 1):
        print("  %d. %s" % (i, e["name"]))


if __name__ == "__main__":
    main()
