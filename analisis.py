import pandas as pd
from modules.data_process import cargar_datos, limpiar_nulos

def realizar_analisis_taller():
    print("\n" + "="*50)
    print("📋 TALLER DE ANÁLISIS DE DATOS - BIBLIOTECA")
    print("="*50)

    datos_completos = pd.read_excel('./data/processed/Resultado.xlsx')
    
    datos_completos['return_date'] = pd.to_datetime(datos_completos['return_date'], format='mixed', dayfirst=True)
    datos_completos['loan_date'] = pd.to_datetime(datos_completos['loan_date'], format='mixed', dayfirst=True)
    datos_completos['dias_prestamo'] = (datos_completos['return_date'] - datos_completos['loan_date']).dt.days
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
    

if __name__ == "__main__":
    realizar_analisis_taller()
