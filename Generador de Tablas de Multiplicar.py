# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

def generar_tabla_multiplicar(numero):

    tabla = []
    for i in range(1, 11):
        resultado = numero * i
        tabla.append(f"{numero} x {i} = {resultado}")
    return tabla

def main():
    print("Generador de Tablas de Multiplicar")
    
    while True:
        try:

            numero = int(input("Introduce un número para generar su tabla de multiplicar: "))
            
            tabla = generar_tabla_multiplicar(numero)
            print("\n".join(tabla))
            break
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

main()
