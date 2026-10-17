# NYC Taxi Analytics

Proyecto inicial para la extracción, limpieza y análisis de datos de viajes de taxis de la ciudad de Nueva York (NYC).

## Estado del proyecto

Este repositorio se encuentra en una etapa temprana de construcción. La estructura base ya incluye:

- extracción de archivos parquet desde el origen de TLC/NYC Taxi
- almacenamiento de datos crudos en la carpeta `data/`
- preparación para transformación y limpieza en `src/transform.py`
- consultas SQL en `queries/clean_taxi_data.sql`

La idea general del pipeline es:

1. Descargar los datos de viajes por mes.
2. Guardarlos en formato parquet en `data/raw`.
3. Limpiar y transformar la información.
4. Preparar consultas analíticas para responder indicadores de movilidad y performance.

## Estructura del repositorio

```text
.
├── data/
│   └── raw/                    # archivos parquet descargados
├── queries/
│   └── clean_taxi_data.sql     # consultas de limpieza/transformación SQL
├── src/
│   ├── config.py               # configuración del proyecto
│   ├── extract.py              # lógica de extracción de datos
│   └── transform.py            # lógica de transformación futura
├── docker-compose.yml          # base para servicios auxiliares
├── requirements.txt            # dependencias del proyecto
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.x
- pip
- Docker (opcional, para levantar servicios adicionales si se agregan más componentes)

## Configuración inicial

1. Clonar el proyecto.
2. Crear un entorno virtual (opcional, pero recomendado).
3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

> La lista de dependencias se completará a medida que el pipeline avance.

## Ejecución actual

El extractor base se ejecuta desde el módulo `src/extract.py`:

```bash
python src/extract.py
```

Actualmente, ese script está configurado para generar URLs de descarga para varios meses del año 2023 y descargar archivos parquet en la carpeta `data/raw`.

## Pipeline propuesto

El flujo esperado del proyecto es:

```text
Fuente TLC / NYC Taxi
        ↓
Extracción (extract.py)
        ↓
Datos crudos en data/raw
        ↓
Transformación y limpieza (transform.py)
        ↓
Consultas SQL (queries/clean_taxi_data.sql)
        ↓
Análisis y reportes
```

## Próximos pasos

- Completar la lógica de generación de URLs en `src/extract.py`.
- Implementar la descarga segura de archivos parquet con validación.
- Definir la estructura de la carpeta `data/processed`.
- Construir la limpieza de columnas y tipos de datos en `src/transform.py`.
- Agregar tests, validación y queries analíticas.

## Nota

Este README es un documento parcial del proyecto y se irá ampliando a medida que el pipeline y la infraestructura queden definidos.
