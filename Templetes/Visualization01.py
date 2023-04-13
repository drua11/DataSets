# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer la base de datos
df = pd.read_csv('nombre_del_archivo.csv')  # Reemplaza 'nombre_del_archivo.csv' con el nombre de tu archivo CSV o el método adecuado para leer tu tipo de archivo

# Explorar los datos
print("Información del DataFrame:")
print(df.info())  # Mostrar información general del DataFrame
print("\nPrimeras filas del DataFrame:")
print(df.head())  # Mostrar las primeras filas del DataFrame
print("\nResumen estadístico del DataFrame:")
print(df.describe())  # Mostrar un resumen estadístico del DataFrame

# Visualizaciones de datos
# Ejemplo de visualización 1: Gráfico de barras
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.countplot(x='columna1', data=df)  # Reemplaza 'columna1' con el nombre de la columna que deseas visualizar
plt.title('Título del gráfico')  # Título del gráfico
plt.xlabel('Etiqueta del eje X')  # Etiqueta del eje X
plt.ylabel('Etiqueta del eje Y')  # Etiqueta del eje Y
plt.show()  # Mostrar el gráfico

# Ejemplo de visualización 2: Gráfico de dispersión
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.scatterplot(x='columna1', y='columna2', data=df)  # Reemplaza 'columna1' y 'columna2' con los nombres de las columnas que deseas visualizar en el eje X y eje Y, respectivamente
plt.title('Título del gráfico')  # Título del gráfico
plt.xlabel('Etiqueta del eje X')  # Etiqueta del eje X
plt.ylabel('Etiqueta del eje Y')  # Etiqueta del eje Y
plt.show()  # Mostrar el gráfico

# Ejemplo de visualización 3: Gráfico de pastel
plt.figure(figsize=(10, 6))  # Tamaño de la figura
df['columna3'].value_counts().plot.pie(autopct='%1.1f%%')  # Reemplaza 'columna3' con el nombre de la columna que deseas visualizar como un gráfico de pastel
plt.title('Título del gráfico')  # Título del gráfico
plt.show()  # Mostrar el gráfico

# Ejemplo de visualización 4: Gráfico de línea
plt.figure(figsize=(10, 6))  # Tamaño de la figura
sns.lineplot(x='columna1', y='columna2', data=df)  # Reemplaza 'columna1' y 'columna2' con los nombres de las columnas que deseas visualizar en el eje X y eje Y, respectivamente
plt.title('Título del gráfico')  # Título del gráfico
plt.xlabel('Etiqueta del eje X')  # Etiqueta del eje X
plt.ylabel('Etiqueta del eje Y')  # Etiqueta del eje Y
plt.show()  # Mostrar el gráfico
