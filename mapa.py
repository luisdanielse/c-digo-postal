# Importar las librerías necesarias
import pandas as pd
import folium
from folium.plugins import HeatMap

# Cargar el archivo Excel con los datos
archivo_excel = "codigos_geolocalizados.xlsx"
datos = pd.read_excel(archivo_excel)

# Ver las columnas que tiene el archivo
print("Las columnas que hay son:", datos.columns)

# Definir las columnas que necesitamos
columnas_que_necesito = ['Lat_A', 'Lon_A', 'Lat_B', 'Lon_B']

# Chequear si las columnas que necesito están en el archivo
for columna in columnas_que_necesito:
    if columna not in datos.columns:
        print(f"¡Ups! La columna {columna} no está en el archivo.")
        exit()  # Salir si falta alguna columna

# Eliminar filas donde falten datos en las columnas que necesito
datos = datos.dropna(subset=columnas_que_necesito)

# Convertir las columnas de latitud y longitud a números
for columna in columnas_que_necesito:
    datos[columna] = pd.to_numeric(datos[columna], errors='coerce')

# Eliminar filas donde no se pudo convertir a número
datos = datos.dropna(subset=columnas_que_necesito)

# Juntar las coordenadas de Lat_A y Lon_A con Lat_B y Lon_B
coordenadas_A = datos[['Lat_A', 'Lon_A']].values.tolist()
coordenadas_B = datos[['Lat_B', 'Lon_B']].values.tolist()
todas_las_coordenadas = coordenadas_A + coordenadas_B

# Calcular el promedio de las latitudes y longitudes para centrar el mapa
latitud_promedio = datos['Lat_A'].mean()
longitud_promedio = datos['Lon_A'].mean()

# Crear el mapa centrado en el promedio de las coordenadas
mapa = folium.Map(location=[latitud_promedio, longitud_promedio], zoom_start=10)

# Agregar el HeatMap al mapa
HeatMap(todas_las_coordenadas).add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapa.html")

print("El mapa se ha creado. Abre 'mapa.html' en tu navegador para verlo.")

