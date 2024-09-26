# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

def contar_palabras(texto):
    palabras = texto.split()  
    return len(palabras)

def main():
    texto = input("Introduce una cadena de texto: ")
    cantidad_palabras = contar_palabras(texto)
    print(f"La cantidad de palabras es: {cantidad_palabras}")

main()