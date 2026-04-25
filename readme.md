# 📚 Sistema de Gestión y Análisis de Préstamos - Biblioteca

Este proyecto es una herramienta modular desarrollada en **Python** para el procesamiento, limpieza y análisis estadístico de datos relacionados con préstamos de artículos en una biblioteca. Permite transformar datos brutos en información valiosa sobre el uso de recursos y tendencias de préstamo.

## 🛠️ Tecnologías y Librerías
* **Lenguaje:** Python 3.x
* **Librerías:** * `Pandas`: Utilizada para toda la manipulación, limpieza y análisis de estructuras de datos (DataFrames).
* **Entorno de desarrollo:** Visual Studio Code.

## 📂 Estructura del Proyecto
El código está organizado de forma modular para facilitar el mantenimiento y la escalabilidad:

* **`main.py`**: Punto de entrada principal. Se encarga de la orquestación del flujo: carga, limpieza inicial, estandarización de estados y mezcla de datos de artículos y préstamos.
* **`analisis.py`**: Módulo especializado en la generación de reportes y métricas. Realiza cálculos de tiempos, frecuencias de uso y filtrados específicos por categorías.
* **`modules/data_process.py`**: Capa de lógica de procesamiento que contiene funciones reutilizables para carga segura de CSV, eliminación de nulos y mapeo de valores.
* **`data/raw/`**: Carpeta destinada a los archivos fuente (`articles.csv` y `loans.csv`).

## 🚀 Funcionalidades Clave

### 1. Limpieza y Estandarización
* **Gestión de Nulos:** Eliminación automática de registros incompletos para asegurar la integridad del análisis.
* **Normalización de Texto:** Conversión de nombres y estados a minúsculas y eliminación de espacios en blanco.
* **Mapeo Flexibe:** El sistema unifica diferentes tipos de entradas (Booleanos, strings "1/0", "activo/inactivo") en categorías estándar como `prestado` o `disponible`.

### 2. Análisis de Métricas
* **Frecuencia de Artículos:** Identifica cuál es el artículo más popular de la biblioteca.
* **Cálculo de Tiempos:** Convierte fechas y calcula automáticamente la duración en días de cada préstamo.
* **Agregación por Categoría:** Genera promedios de días de préstamo agrupados por el tipo de artículo (Categoría ID).
* **Filtrado de Activos:** Detección de artículos específicos (ej. Laptops) que se encuentran en estado de préstamo.

## ⚙️ Instalación y Uso

1.  **Clonar el repositorio** y asegúrate de tener instalada la librería `pandas`.
2.  **Preparar los datos**: Coloca tus archivos `articles.csv` y `loans.csv` dentro de la ruta `data/raw/`.
3.  **Configurar entorno (Opcional)**:
    ```bash
    python -m venv venv
    # Activar venv según sistema operativo
    pip install pandas
    ```
4.  **Ejecutar el programa**:
    * Para el flujo general de procesamiento:
        ```bash
        python main.py
        ```
    * Para obtener el reporte estadístico:
        ```bash
        python analisis.py
        ```