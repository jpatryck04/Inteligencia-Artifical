# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

def calcular_imc(peso, altura):
    # Calcular el IMC
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    # Clasificación del IMC según la OMS
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    print("Calculadora de Índice de Masa Corporal (IMC)")
    
    try:
        peso = float(input("Introduce tu peso en kilogramos: "))
        altura_pies = float(input("Introduce tu altura en pies: "))
        
        # Convertir altura de pies a metros
        altura_metros = altura_pies * 0.3048
        
        if peso <= 0 or altura_metros <= 0:
            print("El peso y la altura deben ser valores positivos.")
            return
        
        imc = calcular_imc(peso, altura_metros)
        clasificacion = clasificar_imc(imc)
        
        print(f"Tu IMC es: {imc:.2f}")
        print(f"Clasificación: {clasificacion}")
        
    except ValueError:
        print("Entrada no válida. Por favor, ingresa valores numéricos.")

main()
