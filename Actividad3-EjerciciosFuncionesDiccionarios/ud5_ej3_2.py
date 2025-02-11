#########################################################
#  Haz un programa que incluya una función
#  que determine si un número es primo.
#########################################################

'''
Método que devuelve true si el numero es primo y
false si el numero no es primo
'''
def esPrimo(num):
    if num <= 1:
        return False
    '''
    Los números primos no pueden ser descompuestos en factores más pequeños.
    Únicamente pueden ser descompuestos por el 1 y ellos mismos.
    '''
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

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
Función para pedir una lista de números al usuario.
'''
def pedirLista():
    lista = []
    print("Introduce números para la lista (escribe 'n' para terminar):")
    entrada = 'x'
    while entrada != 'n':
        entrada = input("Introduce un número: ")
        if entrada != 'n' and esNumero(entrada):
            lista.append(int(entrada))
        elif entrada != 'n' and not esNumero(entrada):
            print("Caracter no válido. Por favor, introduce un número.")
    
    return lista


'''
Programa principal: pide una lista y determina qué números son primos.
'''
print("Vamos a ver que numeros de una lista son primos")
lista = pedirLista()
print(f"\nEn la lista: {lista}")
print("Enocntramos los siguientes numeros primos")
for i in range(len(lista)):
    if esPrimo(lista[i]):
        print(f"El número {lista[i]} es primo")
    
print("\nEl resto de numeros introducidos no son primos")
