import pandas as pd
from modules.data_process import cargar_datos, limpiar_nulos, estandarizar_texto


def main():
    df_ventas = cargar_datos("data/raw/ventas.csv")
    df_productos = cargar_datos("data/raw/productos.csv")
    df_ventas = limpiar_nulos(df_ventas)
    df_productos = limpiar_nulos(df_productos)
    
    df_productos = estandarizar_texto(df_productos, "nombre_producto")
    df_productos = estandarizar_texto(df_productos, "categoria")
    df_ventas = estandarizar_texto(df_ventas, "ciudad_cliente")

    print("📊 Productos más frecuentes:")
    print(df_productos["nombre_producto"].value_counts())
if __name__ == "__main__":
    main()