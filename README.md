
# Análisis de Datos con LLaMA 3.1

Este proyecto proporciona una aplicación de **Streamlit** para realizar análisis de datos utilizando el modelo de lenguaje **LLaMA 3.1**. La aplicación permite a los usuarios cargar datos, generar resúmenes e interactuar con un modelo de machine learning que se ejecuta localmente utilizando la aplicación **Ollama**.

## Características

- **Interfaz Web basada en Streamlit**: Una aplicación web fácil de usar para analizar datos.
- **Soporte para DataFrames de Pandas**: Carga y resumen de conjuntos de datos.
- **Integración con LLaMA 3.1 Local (Ollama)**: Consulta un modelo de lenguaje que se ejecuta localmente utilizando la API de Ollama.
- **Resumen Automático de Datos**: La aplicación proporciona un resumen automático del DataFrame, incluyendo el número de filas, columnas y los tipos de datos de cada columna.

## Requisitos

Para ejecutar este proyecto localmente, necesitas tener las siguientes dependencias instaladas:

- `streamlit`
- `pandas`
- `requests`
- La aplicación **Ollama** para ejecutar el modelo **LLaMA 3.1** localmente.

Puedes instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Cómo Ejecutar

1. Instala la aplicación **Ollama** y asegúrate de que el modelo **LLaMA 3.1** está configurado y en ejecución localmente. Para más información sobre cómo configurar Ollama, consulta la [documentación oficial](https://ollama.com/).

2. Clona el repositorio:
    ```bash
    git clone https://github.com/MiguelGasco/LLama3-Chat-with-your-CSV.git
    ```

3. Navega al directorio del proyecto:
    ```bash
    cd tu-repo
    ```

4. Ejecuta la aplicación de Streamlit:
    ```bash
    streamlit run app.py
    ```

## Configuración

La aplicación interactúa con un endpoint de API local proporcionado por **Ollama** que sirve el modelo **LLaMA 3.1**. Por defecto, la URL de la API está configurada en `http://localhost:11434/v1/completions`. Si es necesario, puedes modificar la variable `API_URL` en el archivo `app.py`.

## Funciones

### `query_model(prompt)`

Esta función envía un prompt a la API local de **LLaMA 3.1** (Ollama) y devuelve la respuesta. Utiliza una solicitud `POST` para consultar el modelo.

### `summarize_dataframe(df)`

Esta función toma un **pandas DataFrame** como entrada y devuelve un resumen de su contenido, incluyendo el número de filas y columnas, así como los detalles sobre el tipo de datos de cada columna.

