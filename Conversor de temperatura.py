# Patryck Yandell Jimenez Ogando.     Mat.2023-1953

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_a_kelvin(fahrenheit):
    celsius = fahrenheit_a_celsius(fahrenheit)
    return celsius_a_kelvin(celsius)

def kelvin_a_fahrenheit(kelvin):
    celsius = kelvin_a_celsius(kelvin)
    return celsius_a_fahrenheit(celsius)

def conversor_temperatura():
    print("Conversor de Temperatura")
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Convertir Fahrenheit a Celsius")
    print("3. Convertir Celsius a Kelvin")
    print("4. Convertir Kelvin a Celsius")
    print("5. Convertir Fahrenheit a Kelvin")
    print("6. Convertir Kelvin a Fahrenheit")
    
    opcion = input("Elige una opción: ")

    if opcion == '1':
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C son {fahrenheit:.2f}°F")
    elif opcion == '2':
        fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit}°F son {celsius:.2f}°C")
    elif opcion == '3':
        celsius = float(input("Introduce la temperatura en grados Celsius: "))
        kelvin = celsius_a_kelvin(celsius)
        print(f"{celsius}°C son {kelvin:.2f} K")
    elif opcion == '4':
        kelvin = float(input("Introduce la temperatura en grados Kelvin: "))
        celsius = kelvin_a_celsius(kelvin)
        print(f"{kelvin} K son {celsius:.2f}°C")
    elif opcion == '5':
        fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
        kelvin = fahrenheit_a_kelvin(fahrenheit)
        print(f"{fahrenheit}°F son {kelvin:.2f} K")
    elif opcion == '6':
        kelvin = float(input("Introduce la temperatura en grados Kelvin: "))
        fahrenheit = kelvin_a_fahrenheit(kelvin)
        print(f"{kelvin} K son {fahrenheit:.2f}°F")
    else:
        print("Opción no válida.")

conversor_temperatura()
