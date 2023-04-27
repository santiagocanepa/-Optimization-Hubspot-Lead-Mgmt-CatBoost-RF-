import pandas as pd

archivo_excel = 'C:/Users/Electro-PC/Python/dataset_FQCTOTAL.xlsx'
df = pd.read_excel(archivo_excel)

df = df[(df['Nombre'].str.len() > 2) & (df['Nombre'] != 'Vista previa')].head(500)

# Reemplaza los términos no deseados en la columna 'Zona Horaria' directamente
df['Zona Horaria'] = df['Zona Horaria'].str.replace('UTC -03:00', '').str.replace('UTC -04:00', '').str.replace('América', '').str.replace('Argentina', '').str.replace('(', '').str.replace(')', '')

# Guarda el DataFrame actualizado en un nuevo archivo Excel
df.to_excel('dataset_FQC_1500_1800resultado.xlsx', index=False)
