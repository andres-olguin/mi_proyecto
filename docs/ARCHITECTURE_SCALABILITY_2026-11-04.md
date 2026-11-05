# brief2scope — Arquitectura y escalabilidad basada en evidencia

**Corte:** 2026-11-04 · **Estado:** documento de ingeniería (propuesta) · **Responsabilidad:** revisión técnica humana antes de prometer capacidades.  
**No constituye:** certificación, cumplimiento normativo, validación de mercado ni garantía de producción.

## 1. Línea base comprobada

Prototipo CLI que clasifica líneas etiquetadas como objetivo, actor, requisito o restricción y exporta JSON; no usa inferencia semántica de lenguaje natural.

## 2. Arquitectura objetivo proporcional al problema

Separar extracción, esquema de requisitos, rastreo de fuentes, revisiones y exportación. Mantener CLI y datos locales para la primera fase; una web multiusuario requerirá identidad, control de versiones, permisos de documentos y protección de confidencialidad.

**Principio de evolución:** escalar verticalmente y reducir cuellos de botella medidos antes de añadir infraestructura horizontal, colas y servicios separados. Elegir proveedor según costos, soberanía y operación, no solo prestigio tecnológico.

## 3. Experimentos de escalabilidad y calidad

Medir tamaño de briefs, elementos extraídos, tiempo de extracción, errores de validación y horas ahorradas observadas por usuario, con comparación al proceso manual; no extrapolar productividad sin estudio.

En cada ejecución documentar hardware/runtime, dataset, comandos, carga, fecha, mediana y dispersión. Reportar errores y fallas; la incorporación del presente documento **no** cuenta como ejecución de benchmark.

## 4. Seguridad, titularidad y límites para un piloto

El texto capturado puede ser comercialmente confidencial. Definir clasificación, borrado, control de exportación, comentarios y aprobaciones; un requisito identificado automáticamente nunca implica aceptación contractual.

Requisitos transversales: autenticación/autorización cuando hay cuentas, minimización de datos, backups ensayados, contratos si hay clientes, secretos fuera de GitHub y fuentes con fecha de cada requisito legal. No cambiar titularidad de proyectos académicos ni reutilizar datos de terceros sin derechos.

## 5. Secuencia de trabajo por gates

G1: contrato JSON y trazabilidad por línea. G2: identificadores estables, deduplicación y cambios de estado. G3: importación Word/PDF autorizada y revisión humana. G4: validar agencia/consultora, métricas de tiempo y disposición de pago.

**Criterio de fin de cada gate:** PR o commit, prueba reproducible y reporte explícito de qué fue medido, qué no se comprobó y riesgos P0/P1 abiertos. No asignar fechas ni presupuesto sin datos de capacidad y aprobación.

## 6. Base metodológica

- [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/): fiabilidad, rendimiento, costo, seguridad y operación.
- [OWASP ASVS 5.0](https://asvs.owasp.org/): requisitos de verificación de apps y APIs, según aplicabilidad.
- [NIST SSDF SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final): desarrollo seguro.
- [Google SRE — SLOs](https://sre.google/workbook/implementing-slos/): decisiones de fiabilidad con datos.
- [OpenTelemetry](https://opentelemetry.io/docs/concepts/observability-primer/): métricas, trazas y logs, cuando sean relevantes.

**Fecha de consulta:** 2026-11-04. Son guías generales: ninguna certifica este software ni respalda ventas o rendimiento no medido.
