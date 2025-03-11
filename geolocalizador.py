# Importar las librerías necesarias
import googlemaps
import pandas as pd
import time

# Poner la clave de la API de Google Maps
mi_clave_api = "AIzaSyADHaH5dS31x9b2Kmd0Ca3SVO8k1yfysPE"


cliente_gmaps = googlemaps.Client(key=mi_clave_api)

# Función para obtener la latitud y longitud de un código postal
def conseguir_lat_lon(codigo_postal):
    """Obtiene la latitud y longitud de un código postal usando Google Maps."""
    try:
        # Hacer la solicitud a la API
        resultado = cliente_gmaps.geocode(f"{codigo_postal}, México")
        if resultado:  # Si hay resultados
            ubicacion = resultado[0]["geometry"]["location"]
            latitud = ubicacion["lat"]
            longitud = ubicacion["lng"]
            return pd.Series([latitud, longitud])
        else:  # Si no hay resultados
            print(f"No se encontró nada para {codigo_postal}")
            return pd.Series([None, None])
    except Exception as error:  # Si hay un error
        print(f"¡Hubo un problema con {codigo_postal}! Error: {error}")
        return pd.Series([None, None])


archivo_excel = "datos_limpios.xlsx"
datos = pd.read_excel(archivo_excel)

# Aplicar la función a la columna para obtener latitud y longitud
datos[["Lat_A", "Lon_A"]] = datos["ZIP A"].apply(conseguir_lat_lon)
datos[["Lat_B", "Lon_B"]] = datos["ZIP B"].apply(conseguir_lat_lon)


archivo_guardado = "codigos_geolocalizados.csv"
datos.to_csv(archivo_guardado, index=False)

print(f"✅ ¡Todo listo! Los datos se guardaron en '{archivo_guardado}'.")