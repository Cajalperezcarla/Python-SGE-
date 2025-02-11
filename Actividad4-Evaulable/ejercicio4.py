# #########################################################
#  Ejercicio 4.4: Devuelve por pantalla los siguientes 
#  15 números a partir de un número cualquiera. Elige
#  el número inicial.
#
#  Autor: Carla Cajal Pérez
# #########################################################


'''
Método para pedir un número válido
'''
def pedirNumero():
    num = input("Inserta un numero: ")
    
    while( not esNumero(num)):
        print("Numero no inválido.")
        num = input("Intentalo de nuevo: ")
    return float(num)
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
Programa principal
'''
numero = pedirNumero()
for i in range(1,16): # recorremos desde el 1 hasta el 15 y le sumamos el numero que se ha introducido
    print(f"{numero + i}, ", end = "")