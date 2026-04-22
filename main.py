import pandas as pd
from modules.data_process import cargar_datos, limpiar_nulos, estandarizar_texto, mapear_valores


def main():
    df_prestamos = cargar_datos("data/raw/loans.csv")
    df_articulos = cargar_datos("data/raw/articles.csv")
    df_prestamos = limpiar_nulos(df_prestamos)
    df_articulos = limpiar_nulos(df_articulos)
    
    df_prestamos = estandarizar_texto(df_prestamos, "status")
    df_articulos = estandarizar_texto(df_articulos, "name")
    
    mapa_status = {
        "p": "prestado",
        "d": "disponible",
        "PRESTADO": "prestado",
        "DISPONIBLE": "disponible"
    }
    df_prestamos = mapear_valores(df_prestamos, "status", mapa_status)
    df_merge = pd.merge(df_prestamos, df_articulos, on="item_id")
    
    

    print("Productos más frecuentes:")
    print(df_articulos["name"].value_counts())

    print("Total de prestamos por producto:")
    prestamos_por_producto = df_merge.groupby("name")["item_id"].count()
    print(prestamos_por_producto)

    print("Prestamos de Silla ergonomica:")
    df_sillas = df_merge[df_merge["name"] == "silla ergonómica"]
    print(df_sillas)


   
if __name__ == "__main__":
    main()