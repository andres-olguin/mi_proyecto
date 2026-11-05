# Brief2Scope — Ingeniería de requisitos desde briefs

**Prototipo local para organizar solicitudes comerciales** en una primera lista de objetivos, actores, requisitos y restricciones, con referencias a las líneas del documento de origen.

> **Estado:** CLI Python con extracción **determinista de etiquetas**, no sistema de IA semántica ni herramienta que genere contratos aprobados. Los resultados necesitan interpretación y revisión humana.

## Problema que aborda

Las solicitudes de sitios web, automatizaciones y software llegan en correos o documentos sin formato común. Brief2Scope permite crear un inventario inicial a partir de líneas con un prefijo conocido y exportarlo como JSON estructurado.

## Entrada admitida

```text
Objetivo: Disminuir tiempo de preparación de propuestas
Actor: Ejecutivo comercial
Requisito: Registrar necesidades entregadas por el prospecto
Requisito: Exportar un borrador para revisión
Restricción: No enviar una propuesta sin aprobación
El presupuesto sigue pendiente de confirmar
```

Las cuatro etiquetas se procesan de forma explícita; la línea sin etiqueta se conserva como nota, **no como requisito inferido automáticamente**. El algoritmo admite tildes en etiquetas y conserva el número de línea de origen.

## Ejecutar localmente

**Requisitos:** Python 3.10+, sin servicios externos ni dependencias adicionales.

```bash
python -m src.brief2scope examples/brief_ejemplo.txt
python -m unittest discover -s tests -v
```

La primera instrucción imprime JSON con `objectives`, `actors`, `requirements`, `constraints`, `notes` y `warnings`. Los requisitos reciben IDs `REQ-001`, `REQ-002` etc. El programa rechaza entradas vacías o superiores al límite configurado de caracteres.

## Arquitectura

| Ruta | Componente |
|---|---|
| [`src/brief2scope.py`](src/brief2scope.py) | Parser y CLI |
| [`examples/brief_ejemplo.txt`](examples/brief_ejemplo.txt) | Brief completamente ficticio |
| [`tests/`](tests/) | Validación de etiquetas, casos límite y errores |
| [`.github/workflows/python-tests.yml`](.github/workflows/python-tests.yml) | Comprobación automatizada |
| [`docs/`](docs/) | Estudio de evolución y madurez técnica |

## Límites y privacidad

- No extrae semánticamente requisitos de texto libre sin etiquetar.
- No verifica contradicciones, prioridades, estimaciones de esfuerzo ni aceptación del cliente.
- No sustituye entrevistas, criterios de aceptación o contratos firmados.
- Aunque procesa documentos locales sin servicios externos, un brief puede contener secretos comerciales: proteger sus ficheros y resultados.

## Hoja de ruta

Agregar esquema JSON versionado, estados de revisión, trazabilidad entre requisitos y solicitudes, exportación controlada, pruebas de documentos más complejos y validación de utilidad con agencias y desarrolladores.

[Plan de escalabilidad](docs/ARCHITECTURE_SCALABILITY_2026-11-04.md) · [Estudio de evolución](docs/ESTUDIO_DE_EVOLUCION_2026-10-30.md).

**Titularidad:** confirmar derechos de los briefs de clientes antes de procesarlos o publicarlos.
