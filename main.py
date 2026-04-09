import pandas as pd
from modules.data_process import cargar_datos


def main():
    df_ventas = cargar_datos("data/raw/ventas.csv")
    df_productos = cargar_datos("data/raw/ventas.csv")

if __name__ == "__main__":
    main()