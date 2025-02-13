# #########################################################
#  Ejercicio 4.9: Realiza un programa que, dadas dos
#  fracciones, obtenga las fracciones equivalentes
#  que tengan el mismo denominador siendo éste el
#  mínimo posible
#
#  Autor: Carla Cajal Pérez
# #########################################################
import math

'''
Método para pedir un número válido
'''
def pedirNumero(mensaje):
    num = input(f"Inserta el {mensaje}: ")
    
    while( not esNumero(num)):
        print("Numero inválido.")
        num = input("Intentalo de nuevo: ")

    num = int(num)

    while( num <= 0):
        print("Numero inválido.")
        num = input("Intentalo de nuevo: ")
    return num
'''
Método que devuelve true si el caracter introducido es un numero
y false si el caracter no lo es
'''
def esNumero(num):
    respuesta = True
    if ( not num.isdigit() ):
        respuesta = False
    return respuesta
'''
Método que reduce las fracciones a irreducibles
'''
def reductorDeFracciones(num,den):
    mcd = math.gcd(num,den) # calculamos el maximo comun divisor con la funcion

    fReducida = {
        "numer": num // mcd,
        "denom": den // mcd
    }

    return fReducida

'''
Método que encuentra el mínimo común denominador entre los denoms (mcm)
'''
def mcm(a, b):

    min = abs(a * b) // math.gcd(a, b)
    return min

def fraccionesComunDenom(num1, den1, num2, den2):
    # Reducimos las fracciones
    fReducida1 = reductorDeFracciones(num1,den1)
    fReducida2 = reductorDeFracciones(num2, den2)

    denominadorComun = mcm(fReducida1["denom"], fReducida2["denom"])

    numerado1 = fReducida1["numer"] *(denominadorComun // fReducida1["denom"])
    numerado2 = fReducida2["numer"] *(denominadorComun // fReducida2["denom"])

    return (numerado1, denominadorComun), (numerado2,denominadorComun)


'''
Programa principal
'''
print("Introduce la primera fracción:")
num1 = pedirNumero("numerador 1")
den1 = pedirNumero("denominador 1")

print("\nIntroduce la segunda fracción:")
num2 = pedirNumero("numerador 2")
den2 = pedirNumero("denominador 2")

fraccion1, fraccion2 = fraccionesComunDenom(num1,den1,num2,den2)
print("\nFracción 1 equivalente:", fraccion1[0], "/", fraccion1[1])
print("Fracción 2 equivalente:", fraccion2[0], "/", fraccion2[1])