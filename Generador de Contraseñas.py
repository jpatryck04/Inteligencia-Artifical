# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

import random
import string

def generar_contraseña(longitud):
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("Generador de Contraseñas Seguras")
    
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (mínimo 6): "))
            if longitud < 6:
                print("La longitud de la contraseña debe ser al menos 6 caracteres.")
                continue
            
            contraseña = generar_contraseña(longitud)
            print(f"Tu contraseña generada es: {contraseña}")
            break
            
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

main()
