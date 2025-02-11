import math

def calcular(radio, longitud):

    radio = float(radio)
    longitud = float(longitud)

    area = math.pi * radio ** 2
    longitud = 2 * math.pi * radio

    return area, longitud

print("Introduce el radio: ", end="")
radio = input()

print("Introduce la longitud: ", end="")
longitud = input()

area, longitud = calcular(radio, longitud)

print("El área es", area)
print("La longitud es", longitud)