# Brief2Scope — prototipo local de extracción de requisitos

Proyecto experimental para transformar un brief de texto en una primera lista **revisable** de objetivos, actores, requisitos y restricciones. No utiliza modelos de IA, no valida requisitos con clientes y **no** genera especificaciones contractual o técnicamente aprobadas.

## Estado verificable

- Implementación inicial propuesta: analizador determinista de líneas etiquetadas en Python (biblioteca estándar).
- Entrada local mediante archivo UTF-8; salida JSON a stdout. Sin conexión a servicios externos.
- Mantener el documento original y solicitar revisión humana antes de convertir los hallazgos en un alcance comercial.
- El archivo histórico `app.txt` permanece sin modificaciones para conservar el inicio del repositorio.

## Uso

Requiere Python 3.10+.

```bash
python -m src.brief2scope examples/brief_ejemplo.txt
python -m unittest discover -s tests -v
```

Etiquetas admitidas: `objetivo:`, `actor:`, `requisito:`, `restriccion:` (también acepta tildes). Las líneas sin etiquetas se registran como notas. Las listas no son clasificadas automáticamente ni se interpreta lenguaje natural ambiguo.

**Privacidad:** nunca ingreses datos personales, financieros ni secretos reales en demostraciones públicas. Esta herramienta solo lee el fichero local y escribe a la salida estándar; redireccionar el resultado es decisión del operador.

## Siguientes hitos

1. Definir esquema de requisitos y criterios de aceptación con un cliente de prueba.
2. Validar requisitos repetidos, dependencias y ambigüedades sin generar certezas ficticias.
3. Exportar borradores Markdown/JSON con historial de revisiones.
4. Añadir pruebas de caracteres, tamaños y entradas malformadas; evaluar entrevistas antes de cualquier propuesta comercial.

Consulta también `docs/ESTUDIO_DE_EVOLUCION_2026-10-30.md`.