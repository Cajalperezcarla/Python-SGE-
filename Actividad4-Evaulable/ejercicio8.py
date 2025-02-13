# #########################################################
#  Ejercicio 4.8: Realiza un programa que, dada una 
#  fracción, obtenga la fracción irreducible (la más 
#  simplificada posible). El usuario introducirá el 
#  numerador y denominador y la salida será un diccionario
#  con “Numerador” y “Denominador” como keys.
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

def reductorDeFunciones(num,den):
    mcd = math.gcd(num,den) # calculamos el maximo comun divisor con la funcion

    fReducida = {
        "Numerador": num // mcd,
        "Denominador": den // mcd
    }

    return fReducida

'''
Programa principal
'''
num = pedirNumero("numerador")
den = pedirNumero("denominador")

fraccionIrreducible = reductorDeFunciones(num,den)
print(f"La fraccion reducida es: {fraccionIrreducible['Numerador']} / {fraccionIrreducible['Denominador']}")
