# #########################################################
#  Ejercicio 4.5: Crea una función que, dado un número, 
# calcule el producto de dos números sin utilizar el 
# operador *. Basa tu solución en la definición 
# primitiva de la multiplicación. 
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
    return int(num)
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
Mñetodo que nos multiplica los numeros introducidos sin el signo *
'''
def multiplicar(a,b):
    resultado = 0
    for i in range(abs(b)):
        resultado += a;

    if b < 0:
        resultado = -resultado
    
    return resultado

'''
Programa principal
'''
num1 = pedirNumero()
num2 = pedirNumero()

res = multiplicar(num1,num2)
print(f"El resultado es: {res}")
