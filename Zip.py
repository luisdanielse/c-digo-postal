# Importar la librería pandas
import pandas as pd

# Cargar el archivo Excel con los códigos postales
archivo_excel = 'Zip.xlsx'
datos_postales = pd.read_excel(archivo_excel)  # Ojo aquí, hay un error tipográfico en "read_excel"


datos_postales = datos_postales[pd.to_numeric(datos_postales['ZIP A'], errors='coerce').notna()]
datos_postales = datos_postales[pd.to_numeric(datos_postales['ZIP B'], errors='coerce').notna()]

# Convertir las columnas "ZIP A" y "ZIP B" a números enteros
datos_postales["ZIP A"] = datos_postales["ZIP A"].astype(int)
datos_postales["ZIP B"] = datos_postales["ZIP B"].astype(int)

# Filtrar los códigos postales para que estén en el rango válido (1000 a 99998)
datos_postales = datos_postales[(datos_postales["ZIP A"] >= 1000) & (datos_postales["ZIP A"] <= 99998)]
datos_postales = datos_postales[(datos_postales["ZIP B"] >= 1000) & (datos_postales["ZIP B"] <= 99998)]


archivo_guardado = "datos_limpios.xlsx"
datos_postales.to_excel(archivo_guardado, index=False)


print("Las primeras filas de los datos limpios son:")
print(datos_postales.head())