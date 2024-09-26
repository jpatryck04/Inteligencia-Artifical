# Patryck Yandell Jimenez Ogando.     Mat.2023-1953
import random

def adivina_el_numero():
    
    numero_secreto = random.randint(1, 20)
    intentos = 0
    
    print("¡Bienvenido al juego 'Adivina el Número'!")
    print("He elegido un número entre 1 y 20. ¡Intenta adivinarlo!")

    while True:
        try:
            suposicion = int(input("Introduce tu suposición: "))
            intentos += 1
            
            if suposicion < 1 or suposicion > 20:
                print("¡Fuera del margen de números! Por favor, elige un número entre 1 y 20.")
            elif suposicion < numero_secreto:
                print("Demasiado bajo. Intenta de nuevo.")
            elif suposicion > numero_secreto:
                print("Demasiado alto. Intenta de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

adivina_el_numero()
