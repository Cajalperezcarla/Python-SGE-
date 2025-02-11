# #########################################################
#  Ejercicio 4.3: Dada una longitud y un radio, 
# calcula tanto su área como la longitud de la 
# circunferencia. Considerausar la librería math 
# para trabajar con el valor de pi. 
#
#  Autor: Carla Cajal Pérez
# #########################################################
import math

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
Método que devuelve true si es positivo y false
si el número si no es positivo
'''
def esPositivo(num):
    respuesta = True
    if( num <= '0' ):
        respuesta = False
    return respuesta
'''
Método que calcula el area y la longitud segun el rádio
'''
def calcular(radio):

    radio = float(radio)
    
    area = math.pi * radio ** 2
    longitud = 2 * math.pi * radio

    return area, longitud

'''
Programa principal
'''
radio = input("Introduce el radio: ")
while (not esNumero(radio) or not esPositivo(radio)):
    print("Numero inválido.")
    radio = input("Intentalo de nuevo: ")

# guardamos los datos de area y longitud
area, longitd = calcular(radio)

print("El área es", area)
print("La longitud es", longitud)