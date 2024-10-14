import pandas as pd
import streamlit as st
import requests

API_URL = "http://localhost:11434/v1/completions"
MODEL_NAME = "llama3.1:8b"

st.title("Data Analysis with LLaMA 3.1")

# Función para consultar el modelo
def query_model(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "temperature": 0
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(API_URL, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Crear un resumen del DataFrame
def summarize_dataframe(df):
    summary = f"El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n"
    summary += "Las columnas son:\n"
    
    for col in df.columns:
        col_data = df[col]
        summary += f"- {col} (tipo: {col_data.dtype}):\n"
        
        if pd.api.types.is_numeric_dtype(col_data):
            summary += f"  Media: {col_data.mean()}, Mediana: {col_data.median()}, Desv. estándar: {col_data.std()}\n"
        elif pd.api.types.is_string_dtype(col_data):
            summary += f"  Ejemplos de valores: {col_data.unique()[:5]}\n"
        else:
            summary += f"  Valores únicos: {col_data.nunique()}, Ejemplos de valores: {col_data.unique()[:5]}\n"
    
    return summary

def main():
    dataset = st.file_uploader("Upload your csv file", type=['csv'])
    
    if not dataset:
        st.stop()

    if dataset.name.endswith('.csv'):
        df = pd.read_csv(dataset, low_memory=False)

    st.write("Data Preview:")
    st.dataframe(df.head())

    prompt = st.text_input("Enter your question/prompt.")
    if not prompt:
        st.stop()

    df_summary = summarize_dataframe(df)

    context = f"""Eres un experto en análisis de datos.Primero darás el resultado a la pregunta y después daras el código que has utilizado.
     Aquí está un resumen del DataFrame:\n{df_summary}\n y aquí el DataFrame entero: {df}.Cuando des el código, en la parte de pd.read_csv(), dentro pon el siguiente nombre: {dataset.name}"""
    query = f"{context}. Ahora responde a esta pregunta, {prompt}"

    response = query_model(query)

    st.write("La solución puede ser errónea:")
    st.write(response)

if __name__ == '__main__':
    main()