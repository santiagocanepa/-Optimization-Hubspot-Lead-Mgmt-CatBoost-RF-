import pandas as pd

# Leer el archivo de Excel
db = 'C:/Users/Santiago/Py/dataset_FQC_1800.xlsx'
df = pd.read_excel(db)

# Filtra las filas
df = df[(df['Nombre'].str.len() > 2) & (df['Nombre'] != 'Vista previa')]

df = df.head(500)

# Guarda el resultado en un nuevo archivo de Excel
df.to_excel('dataset_FQC_1800.xlsx', index=False)
