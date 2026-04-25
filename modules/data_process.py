import pandas as pd
import os
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

def estandarizar_texto(df, columna):
    df[columna] = df[columna].astype(str).str.lower().str.strip()
    return df

def mapear_valores(dataframe, columna, diccionario):
    if dataframe is not None and columna in dataframe.columns:
        dataframe[columna] = dataframe[columna].replace(diccionario)
        print(f"Valores de '{columna}' estandarizados.")
        return dataframe
    return dataframe

def crear_Archivo(dataframe):
    ruta = "./data/procesed"
    try:
        os.mkdir(ruta)
    except:
        print('Ya existia ruta')
    finally:
        dataframe.to_excel(f'{ruta}/Resultado.xlsx',index=False)