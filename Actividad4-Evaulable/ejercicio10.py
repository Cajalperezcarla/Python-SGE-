# #########################################################
#  Ejercicio 4.10: Realiza una calculadora de fracciones. 
#  Debe poder sumar, restar, multiplicar y dividir dos 
#  fracciones. El resultado debe ser una fracción irreducible.
#  En este caso, como el resultado poder ser negativo, 
#  debemos usar una función matemática que nos dé el
#  valor absoluto de un número, dicha función es abs(número).
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
Método que reduce una fracción a su forma irreducible
'''
def reducirFraccion(num, den):
    mcd = math.gcd(num, den)  # Calculamos el Máximo Común Divisor
    num //= mcd
    den //= mcd
    if den < 0:  # Asegurar que el denominador siempre sea positivo
        num = -num
        den = abs(den)
    return num, den

'''
Método para mostrar el menú
'''
def menu():
    print("Elige una opción (1,2,3,4 o 5)")
    print("\n\t1. Sumar fracciones")
    print("\t2. Restar fracciones")
    print("\t3. Multiplicar fracciones")
    print("\t4. Dividir fracciones")
    print("\t5. Salir")
    opcion = input("Eligue una opcion: ")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        opcion = -1
    return opcion
'''
Método que permite sumar dos fracciones
'''
def sumarFracciones(num1, den1, num2, den2):
    num = num1 * den2 + num2 * den1
    den = den1 * den2
    return reducirFraccion(num,den)
'''
Método que permite restar dos racciones
'''
def restarFracciones(num1, den1, num2, den2):
    num = num1 * den2 - num2 * den1
    den = den1 * den2
    return reducirFraccion(num, den)
'''
Método que permite multiplicar dos fracciones
'''
def multiplicacionFracciones(num1, den1, num2, den2):
    num = num1 * num2
    den = den1 * den2
    return reducirFraccion(num,den)
'''
Método que permite dividir dos fracciones
'''
def divisionFracciones(num1, den1, num2, den2):
    num = num1 * den2
    den = den1 * num2
    reducirFraccion(num,den)

'''
Programa principal
'''
print("Vamos a calcular alguna operacion con fracciones! ")
print("Primero necesito que escribas las fracciones,\ndespues elijirás la opción que deseas hacer")
num1 = pedirNumero("numerador 1")
den1 = pedirNumero("denominador 1")
num2 = pedirNumero("numerador 2")
den2 = pedirNumero("denominador 2")
opcion = 0
while opcion != 5:
    opcion = menu()
    if( opcion == 1 ):
        resultado = sumarFracciones(num1,den1,num2,den2)
        print(f"Resultado de la suma: {resultado[0]} / {resultado[1]}")
    elif( opcion == 2):
       resultado = restarFracciones(num1,den1,num2,den2)
       print(f"Resultado de la resta: {resultado[0]} / {resultado[1]}")
    elif( opcion == 3):
        resultado = multiplicacionFracciones(num1,den1,num2,den2)
        print(f"Resultado de la multiplicación: {resultado[0]} / {resultado[1]}")
    elif( opcion == 4):
       resultado = divisionFracciones(num1,den1,num2,den2)
       print(f"Resultado de la division: {resultado[0]} / {resultado[1]}")
    elif(opcion == 5):
        print("Hasta luego!!")
    else:
        print("Opcion no válida")