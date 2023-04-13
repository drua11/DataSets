# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np

# Cargar los datos en un DataFrame
df = pd.read_csv('ruta/del/archivo.csv')

# Revisar la información general del DataFrame
print("Información general del DataFrame:")
print(df.info())

# Visualizar las primeras filas del DataFrame
print("\nPrimeras filas del DataFrame:")
print(df.head())

# Resumen estadístico del DataFrame
print("\nResumen estadístico del DataFrame:")
print(df.describe())

# Verificar y manejar valores nulos o faltantes
print("\nValores nulos o faltantes:")
print(df.isnull().sum())  # Verificar valores nulos
df.dropna(inplace=True)  # Eliminar filas con valores nulos

# Verificar y manejar duplicados
print("\nDuplicados:")
print(df.duplicated().sum())  # Verificar duplicados
df.drop_duplicates(inplace=True)  # Eliminar duplicados

# Manipulación de columnas
print("\nManipulación de columnas:")
df.drop('nombre_de_columna', axis=1, inplace=True)  # Eliminar columna
df['nueva_columna'] = df['columna_existente'] * 2  # Crear nueva columna
df.rename(columns={'nombre_antiguo': 'nombre_nuevo'}, inplace=True)  # Renombrar columna

# Filtrar y seleccionar datos
print("\nFiltrar y seleccionar datos:")
df_filtrado = df[df['columna'] > valor]  # Filtrar por una condición
columnas_seleccionadas = df[['columna1', 'columna2']]  # Seleccionar columnas específicas

# Ordenar datos
print("\nOrdenar datos:")
df.sort_values('columna', ascending=False, inplace=True)  # Ordenar por columna en orden descendente

# Agregación y resumen de datos
print("\nAgregación y resumen de datos:")
df_agregado = df.groupby('columna').mean()  # Agrupar y obtener promedio de columnas numéricas

# Visualización de datos
# Utilizar bibliotecas de visualización de datos como Matplotlib, Seaborn o Plotly para crear gráficos y visualizar los datos.

