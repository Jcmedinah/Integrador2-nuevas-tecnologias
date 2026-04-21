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

    df_merge = pd.merge(df_ventas, df_productos, on="id_producto")

    print("📊 Productos más frecuentes:")
    print(df_productos["nombre_producto"].value_counts())
   
    print("\n📊 Total de ventas por producto:")
    ventas_por_producto = df_merge.groupby("nombre_producto")["cantidad"].sum()
    print(ventas_por_producto)

    print("\n📍 Ventas en Medellín:")
    df_medellin = df_merge[df_merge["ciudad_cliente"] == "medellin"]
    print(df_medellin)

if __name__ == "__main__":
    main()