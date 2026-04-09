import pandas as pd
def cargar_datos(ruta_archivo):
    try:
        dataframe = pd.read_csv(ruta_archivo)
        print(f"✅ Archivo '{ruta_archivo}' cargado con éxito.")
        return dataframe
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta '{ruta_archivo}'. Verifica la carpeta data/.")
        return None
    
def limpiar_nulos(dataframe):
    if dataframe is not None:
        df_limpio = dataframe.dropna()
        print("Valores nulos eliminados")
        return df_limpio
    return None