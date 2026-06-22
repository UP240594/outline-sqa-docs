[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=wiki-sqa_wiki-analisis&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=wiki-sqa_wiki-analisis)
# outline-sqa-docs

El siguiente repositiorio tiene como objetivo tener una documentacion del trabajo que cada quien hizo en el equipo, teniendo como objetivo una mayor organizacion en el equipo, a continuacion se mencionan de lo que se encargara cada quien en el proyecto, se subiran los cambios al repositiorio aqui, tanto su formato tex como pdf, para al final unir el trabajo y subirlo al apartado correspondiente.

En el entregable anterior nos enfocamos en encontrar metricas y estandares que cumplieran ciertas normas, ahora nos enfocaremos a medir el codigo de nuestro codigo haciendo como testers y haciendo pruebas con sonarqube y selenium, las partes de cada quien estuvieron distribuidas en base al documento proporcionado por el profesor

# Roles y cosas que le toca a cada uno: #

### Odin: Investigador de Herramientas (Enfoque Teórico)
> **Responsable de las secciones 4.1 y 4.2**

* Comparar al menos tres frameworks E2E y tres herramientas de análisis estático.
* Crear una tabla comparativa de herramientas E2E incluyendo criterios como lenguajes soportados, curva de aprendizaje y soporte de navegadores.
* Explicar los defectos que detecta el análisis estático frente al dinámico.
* Redactar las recomendaciones justificadas para la Wiki utilizando citas en formato APA.

---

### Alan: Ingeniero E2E - Arquitectura y Page Object Model
> **Responsable de la sección 4.3 (Parte 1)**

* Estructurar el proyecto de pruebas creando los directorios `pages/`, `tests/` y el archivo `conftest.py`.
* Programar al menos 2 *Page Objects* con sus respectivos localizadores y métodos de negocio para la Wiki.
* Implementar al menos 5 pruebas automatizadas que abarquen casos válidos, de frontera y de error.
* Utilizar exclusivamente esperas explícitas de Selenium, evitando `time.sleep`.

---

### Olivia: Ingeniera E2E - Pruebas Data-driven e Integración Continua
> **Responsable de las secciones 4.3 (Parte 2) y 4.5**

* Desarrollar al menos 1 prueba data-driven utilizando el decorador `@pytest.mark.parametrize`.
* Capturar la salida de las pruebas y generar el reporte HTML de pytest.
* Configurar el pipeline de Integración Continua, incluyendo el archivo YAML y la captura de su ejecución.
* Documentar las condiciones del *Quality Gate* y explicar bajo qué escenarios bloquearía un merge.

---

### Noe: Analista de SonarQube y Cobertura
> **Responsable de la sección 4.4**

* Configurar el archivo `sonar-project.properties` para la Wiki y tomar captura del tablero resultante.
* Reportar los ratings obtenidos en las cinco dimensiones de calidad: *Reliability, Security, Maintainability, Coverage* y *Duplications*.
* Analizar a detalle al menos 3 issues detectados, documentando su tipo, severidad, línea de código y explicación.
* Asegurar la conexión de la cobertura generada por pytest mediante `coverage.xml`.

---

### Omar: Gestor de Deuda Técnica y Maestro del Documento
> **Responsable de la sección 4.6 y la consolidación del entregable**

* Elaborar la tabla de remediación de deuda técnica tomando los issues de SonarQube e indicando severidad, esfuerzo estimado, prioridad y responsable.
* Justificar la prioridad de los issues basándose estrictamente en severidad e impacto, aplicando el enfoque *Clean as You Code*.
* Consolidar el documento final y compilarlo en LaTeX, asegurando los márgenes de 2.5 cm, tipografía Latin Modern y el estilo de citación APA.
* Generar los archivos finales para la entrega en Classroom (`.pdf`, `.tex` y `.zip`).
## Estructura de carpetas
 - /Olivia
 - /Noe
 - /Omar
 - /Alan
 - /Odin


## Comandos básicos git
- git pull origin main
- git add .
- git commit -m "breve descripción"
- git push origin main

  # Nota:
  Se creearan carpetas para organizar y poner la parte de cada uno ahi, en caso de hacer cualquier cambio, o no documentar este mismo por olvido de un git push, favor de aclararlo.  #    
