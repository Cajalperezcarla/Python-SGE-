from math import gcd

def obtener_mcm(a, b):
    # Calcula el mínimo común múltiplo (mcm)
    return abs(a * b) // gcd(a, b)

def fracciones_equivalentes(fraccion1, fraccion2):
    num1, den1 = fraccion1
    num2, den2 = fraccion2
    
    mcm_denominador = obtener_mcm(den1, den2)
    
    num1_equivalente = num1 * (mcm_denominador // den1)
    num2_equivalente = num2 * (mcm_denominador // den2)
    
    print("Fracciones originales:")
    print(f"{num1}/{den1} y {num2}/{den2}")
    
    print("\nFracciones equivalentes con denominador mínimo común:")
    print(f"{num1_equivalente}/{mcm_denominador} y {num2_equivalente}/{mcm_denominador}")

fraccion1 = (3, 4)
fraccion2 = (5, 6)
fracciones_equivalentes(fraccion1, fraccion2)
