# NYC Taxi Analytics

Proyecto inicial para la extracción, limpieza y análisis de datos de viajes de taxis de la ciudad de Nueva York (NYC).

## Estado del proyecto

Este repositorio se encuentra en una etapa temprana de construcción. La estructura base incluye:

- un esqueleto para extraer archivos Parquet de TLC/NYC Taxi (`src/extract.py`)
- las carpetas `data/`, `src/` y `queries/` para organizar el proyecto
- archivos iniciales para configuración, transformación y consultas SQL

La extracción y transformación todavía no están implementadas por completo. El flujo previsto es:

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

## Requisitos previos

- Python 3.8 o superior y `pip`.
- Docker es opcional; por ahora no es necesario para ejecutar el código disponible.

## Instalación

Desde la raíz del repositorio, crea y activa un entorno virtual:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instala las dependencias declaradas:

```bash
pip install -r requirements.txt
```

El extractor importa `requests`. Si aún no está incluido en `requirements.txt`, instálalo en el entorno virtual con:

```bash
python -m pip install requests
```

## Estado y ejecución

El punto de entrada previsto para la extracción es:

```bash
python src/extract.py
```

**La extracción aún no puede ejecutarse correctamente:** `generate_urls` y `download_parquet` en `src/extract.py` contienen marcadores `TODO` pendientes de implementación. Cuando estén implementados, se podrán cambiar el año y los meses en el bloque `if __name__ == "__main__"` del script.

Ten en cuenta que la ruta de salida actual (`../data/raw`) es relativa al directorio desde el que se ejecuta el comando. Ejecutándolo desde la raíz del repositorio, apunta a una carpeta `data/raw` en el directorio padre, no a `data/raw` dentro del repositorio. Ajusta esa ruta en el script antes de descargar datos para guardarlos en la ubicación esperada.

Los archivos Parquet descargados son datos de entrada y pueden ocupar mucho espacio. Comprueba que la carpeta de destino tenga espacio suficiente y evita subir los datos al repositorio si no corresponde.

## Estructura de datos prevista

- `data/raw/`: archivos Parquet originales descargados.
- `data/processed/`: datos limpiados y transformados; esta carpeta aún debe definirse e implementarse.
- `queries/clean_taxi_data.sql`: espacio para las consultas de limpieza/transformación SQL.

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

- Completar la generación de URLs y la descarga con validación en `src/extract.py`.
- Corregir y centralizar la configuración de las rutas de datos.
- Definir `data/processed/` e implementar la limpieza de columnas y tipos en `src/transform.py`.
- Completar las consultas SQL y agregar pruebas y validaciones.

## Nota

Este README es un documento parcial del proyecto y se irá ampliando a medida que el pipeline y la infraestructura queden definidos.
