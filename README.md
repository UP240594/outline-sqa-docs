[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wiki-sqa_wiki-analisis&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wiki-sqa_wiki-analisis)

# 📘 outline-sqa-docs

Repositorio oficial del **Equipo 4** (TIID05B) para la asignatura **Estándares y Métricas para el Desarrollo de Software**.
Contiene la documentación completa del proyecto integrador **Outline** (wiki interna estilo Notion), incluyendo:

- Análisis de calidad según **ISO/IEC 25010:2023**.
- Plan SQA basado en **IEEE 730-2014**.
- **KPIs** y métricas reportables (ISO 25023, ISO 5055).
- **Matriz de trazabilidad** requisito → caso de prueba → defecto → métrica.
- **Ejemplos reales** de informes QA (SonarQube y Selenium).
- **Resultados prácticos** del análisis estático (SonarQube) y pruebas E2E (Selenium) realizados en el Examen Práctico de la Unidad 2.
- **Reporte integrador** en formato LaTeX (PDF + `.tex`) y evidencias en `.zip`.

---

## 📁 Estructura del repositorio

```
outline-sqa-docs/
├── README.md
├── Metricas y Estandares/        # Entregables anteriores (Tarea 03, etc.)
├── Tarea09/                      # Documentación de la calidad (entrega final)
│   ├── Olivia/                   # Portada, introducción, conclusión, referencias
│   ├── Alan/                     # Secciones 4.1 y 4.2 (estándares y anatomía)
│   ├── Omar/                     # Secciones 4.3 y 4.5 (trazabilidad y ejemplos)
│   ├── Noe/                      # Sección 4.4 (métricas y KPIs)
│   ├── Odin/                     # Sección 4.6 (aplicación y resultados)
│   ├── TIID05B_Equipo4_Sem11.tex # Documento unificado (compilable)
│   └── TIID05B_Equipo4_Sem11.pdf # Versión final en PDF
└── Evidencias_P2/                # Scripts de Selenium + reportes (coverage.xml, report.html)
```

---

## 👥 Roles y responsabilidades (Tarea 09)

| Integrante | Rol | Secciones a cargo |
|------------|-----|-------------------|
| **Olivia Chairez** | Coordinadora | Portada, índice, introducción, conclusión, referencias APA 7, unificación del documento en LaTeX y empaquetado del `.zip` con evidencias del P2. |
| **Alan Jauregui** | Documentador | **4.1** – Comparativa de estándares (IEEE 730, ISO 29119, IEEE 829) <br> **4.2** – Anatomía del informe de calidad (SQA) y de pruebas. |
| **Omar Facio** | QA Tester | **4.3** – Matriz de trazabilidad con ejemplo basado en HU-01 (Outline). <br> **4.5** – Comparativa de reportes reales (SonarQube vs Selenium). |
| **Noé Estrada** | Líder / Analista | **4.4** – Métricas reportables (McCabe, Halstead, IFPUG, cobertura, densidad de defectos) vinculadas a ISO 25010:2023 y umbrales de referencia. |
| **Odin Rubio** | Developer | **4.6** – Índice comentado del reporte integrador, redacción de introducción, alcance y metodología; consolidación de métricas del Examen P2 (cobertura 62%, deuda técnica 23 días, 42/42 pruebas pasadas, Quality Gate aprobado). |

---

## 🔧 ¿Qué contiene este repositorio?

- **Documentación normativa**: Aplicación de estándares ISO/IEC 25010, IEEE 730, ISO/IEC 29119, IEEE 829.
- **Métricas cuantitativas**: KPIs definidos para Outline, cobertura de código, deuda técnica, densidad de defectos.
- **Pruebas automatizadas**: Scripts de Selenium (Page Object Model, esperas explícitas, pruebas parametrizadas) y análisis estático con SonarQube (reporte de issues y Quality Gate).
- **Evidencias**: Capturas de pantalla, reportes HTML y XML generados durante la ejecución de pruebas.
- **Informe final**: Documento unificado en LaTeX (formato APA 7) que integra todas las secciones y referencias.

---

## 🚀 Cómo contribuir

1. **Clona** el repositorio:
   ```bash
   git clone https://github.com/UP240594/outline-sqa-docs.git
   ```

2. Crea una rama para tu trabajo:
   ```bash
   git checkout -b tu-nombre/seccion
   ```

3. Sube tus cambios a tu carpeta personal (`/TuNombre/`) y actualiza el archivo principal si es necesario.

4. Haz un pull request o avisa al equipo para revisar y fusionar.

---

## 📦 Entregable final

- **PDF:** `TIID05B_Equipo4_Sem11.pdf`
- **Código fuente LaTeX:** `TIID05B_Equipo4_Sem11.tex`
- **Evidencias comprimidas:** `TIID05B_Equipo4_Sem11.zip` (contiene scripts de Selenium + reportes de cobertura y SonarQube)

---

## 📌 Notas importantes

- El repositorio es privado y solo tienen acceso los miembros del equipo y el profesor.
- Todas las referencias bibliográficas están en formato APA 7 y se incluyen dentro del documento LaTeX (no se requiere archivo `.bib` externo).
- El análisis de SonarQube se realizó sobre el código de Outline, y el estado del Quality Gate se refleja en el badge al inicio de este README.
