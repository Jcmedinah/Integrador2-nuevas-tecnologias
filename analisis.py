import pandas as pd
from modules.data_process import cargar_datos, limpiar_nulos

def realizar_analisis_taller():
    print("\n" + "="*50)
    print("📋 TALLER DE ANÁLISIS DE DATOS - BIBLIOTECA")
    print("="*50)

    articulos = cargar_datos("data/raw/articles.csv")
    prestamos = cargar_datos("data/raw/loans.csv")

    articulos = limpiar_nulos(articulos)
    prestamos = limpiar_nulos(prestamos)

    prestamos['loan_date'] = pd.to_datetime(prestamos['loan_date'], dayfirst=True, errors='coerce')
    prestamos['return_date'] = pd.to_datetime(prestamos['return_date'], dayfirst=True, errors='coerce')

    prestamos['dias_prestamo'] = (prestamos['return_date'] - prestamos['loan_date']).dt.days

    datos_completos = pd.merge(prestamos, articulos, on="item_id")

    frecuencia = datos_completos['name'].value_counts()
    articulo_frecuente = frecuencia.idxmax()
    total_veces = frecuencia.max()

    print(f"\n✅ 1. ANÁLISIS DE FRECUENCIA:")
    print(f"   - El artículo más popular es: '{articulo_frecuente}'")
    print(f"   - Se ha prestado un total de {total_veces} veces.")

    promedio_por_cat = datos_completos.groupby('category_id')['dias_prestamo'].mean()

    print(f"\n✅ 2. ANÁLISIS DE AGREGACIÓN:")
    print("   - Promedio de días que se presta cada tipo de artículo (por ID de Categoría):")

    print(promedio_por_cat.round(1))

    laptops_prestadas = datos_completos[
        (datos_completos['category_id'] == '1') & 
        (datos_completos['return_date'].isna())
    ]
    conteo_laptops = len(laptops_prestadas)

    print(f"\n✅ 3. ANÁLISIS CON FILTRADO:")
    print(f"   - Actualmente hay {conteo_laptops} Laptops (Categoría 1) que no han sido devueltas.")
    
    print("\n" + "="*50)
    print("🏁 FIN DEL ANÁLISIS - CÓDIGO LISTO PARA ENTREGAR")
    print("="*50)

if __name__ == "__main__":
    realizar_analisis_taller()
