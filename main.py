import pandas as pd
from modules.data_process import cargar_datos, limpiar_nulos, estandarizar_texto


def main():
    df_prestamos = cargar_datos("data/raw/articles.csv")
    df_articulos = cargar_datos("data/raw/loans.csv")
    df_prestamos = limpiar_nulos(df_prestamos)
    df_articulos = limpiar_nulos(df_articulos)
    
    # df_prestamos = estandarizar_texto(df_prestamos, "status")
    # df_articulos = estandarizar_texto(df_articulos, "name")
    
    df_merge = pd.merge(df_prestamos, df_articulos, on="item_id")
    print(df_merge)
    print("📊 Productos más frecuentes:")
    print(df_articulos["name"].value_counts())

    print("\n📊 Total de ventas por producto:")
    ventas_por_producto = df_merge.groupby("nombre_producto")["cantidad"].sum()
    print(ventas_por_producto)

    print("\n📍 Ventas en Medellín:")
    df_medellin = df_merge[df_merge["ciudad_cliente"] == "medellin"]
    print(df_medellin)

    print("Productos más frecuentes:")
    print(df_articulos["name"].value_counts())
if __name__ == "__main__":
    main()