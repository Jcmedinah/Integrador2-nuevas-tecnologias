import pandas as pd
from modules.data_process import cargar_datos, limpiar_nulos


def main():
    df_ventas = cargar_datos("data/raw/ventas.csv")
    df_productos = cargar_datos("data/raw/productos.csv")
    df_ventas = limpiar_nulos(df_ventas)
    df_productos = limpiar_nulos(df_productos)

if __name__ == "__main__":
    main()