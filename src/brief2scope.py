"""Extractor experimental de requisitos etiquetados; sin inferencia automática."""
import argparse
import json
from pathlib import Path
import sys
import unicodedata

LABELS = {
    "objetivo": "objectives",
    "actor": "actors",
    "requisito": "requirements",
    "restriccion": "constraints",
}

def normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFD", text.strip().lower())
    return "".join(char for char in decomposed if unicodedata.category(char) != "Mn")

def parse_brief(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("El brief debe ser texto UTF-8.")
    if not text.strip():
        raise ValueError("El brief no puede estar vacío.")
    if len(text) > 100_000:
        raise ValueError("El brief excede el límite de 100.000 caracteres.")
    result = {"objectives": [], "actors": [], "requirements": [], "constraints": [], "notes": [], "warnings": []}
    for line_number, original in enumerate(text.splitlines(), start=1):
        line = original.strip()
        if not line or line.startswith("#"):
            continue
        prefix, separator, value = line.partition(":")
        key = LABELS.get(normalize(prefix)) if separator else None
        if key and value.strip():
            entry = {"id": f"REQ-{len(result[key]) + 1:03d}" if key == "requirements" else None,
                     "text": value.strip(), "source_line": line_number}
            if entry["id"] is None:
                del entry["id"]
            result[key].append(entry)
        else:
            result["notes"].append({"text": line, "source_line": line_number})
    if not result["requirements"]:
        result["warnings"].append("No hay requisitos etiquetados; revisión humana necesaria.")
    result["warnings"].append("Borrador sin validación ni aprobación de alcance.")
    return result

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Extrae requisitos etiquetados desde un brief local.")
    parser.add_argument("file", type=Path, help="Archivo UTF-8 de entrada")
    args = parser.parse_args(argv)
    try:
        data = args.file.read_text(encoding="utf-8")
        print(json.dumps(parse_brief(data), ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
