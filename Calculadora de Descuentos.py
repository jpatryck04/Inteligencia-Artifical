# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

def calcular_precio_final(precio_original, porcentaje_descuento):

    descuento = precio_original * (porcentaje_descuento / 100)

    precio_final = precio_original - descuento
    return precio_final

def main():
    print("Calculadora de Descuentos")
    
    try:

        precio_original = float(input("Introduce el precio original del artículo: "))
        porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))
        
        if precio_original < 0 or porcentaje_descuento < 0:
            print("El precio y el porcentaje de descuento deben ser valores no negativos.")
            return
        
        precio_final = calcular_precio_final(precio_original, porcentaje_descuento)
        
        print(f"El precio final después de aplicar un descuento del {porcentaje_descuento}% es: {precio_final:.2f}")
        
    except ValueError:
        print("Entrada no válida. Por favor, ingresa valores numéricos.")

main()
