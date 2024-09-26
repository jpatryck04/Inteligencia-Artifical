# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

def ordenar_lista(numeros):

    return sorted(numeros)

def main():
    print("Ordenamiento de Listas")
    
    while True:
        try:

            entrada = input("Introduce una lista de números enteros separados por comas: ")

            numeros = [int(num.strip()) for num in entrada.split(',')]
            

            numeros_ordenados = ordenar_lista(numeros)
            
            print(f"Números ordenados de menor a mayor: {numeros_ordenados}")
            break
            
        except ValueError:
            print("Entrada no válida. Por favor, asegúrate de ingresar solo números enteros separados por comas.")

main()
