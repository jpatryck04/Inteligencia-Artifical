# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

import random

def obtener_eleccion_computadora():

    return random.choice(['piedra', 'papel', 'tijeras'])

def determinar_ganador(eleccion_usuario, eleccion_computadora):
    if eleccion_usuario == eleccion_computadora:
        return "Empate"
    elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijeras') or \
         (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
         (eleccion_usuario == 'tijeras' and eleccion_computadora == 'papel'):
        return "Ganaste"
    else:
        return "Perdiste"

def main():
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    
    while True:

        eleccion_usuario = input("Elige piedra, papel o tijeras (o escribe 'salir' para terminar): ").lower()
        
        if eleccion_usuario == 'salir':
            print("¡Gracias por jugar!")
            break
        
        if eleccion_usuario not in ['piedra', 'papel', 'tijeras']:
            print("Elección no válida. Por favor, elige piedra, papel o tijeras.")
            continue
        
        eleccion_computadora = obtener_eleccion_computadora()
        print(f"La computadora eligió: {eleccion_computadora}")
        
        resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
        print(f"Resultado: {resultado}")

main()
