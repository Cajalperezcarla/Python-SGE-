#########################################################
# Haz un programa que incluya una función que calcule
# el área de un círculo dado su radio.
#########################################################
import math
'''
Método que calcula el diametro de la circunferencia
'''
def calculaDiametro(radio):
    diametro = 2 * radio
    return diametro
'''
Método que calcula el area de la circunferencia
'''
def calculaArea(radio):
    area = math.pi * (radio ** 2)
    return area
'''
Método que calcula el perimetro de la circunferencia
'''
def calculaPerimetro(radio):
    perimetro = 2 * math.pi * radio
    return perimetro
'''
Método para pedir un número válido
'''
def pedirNumero():
    num = input("Inserta el tamaño del radio: ")
    
    while( not esNumero(num) or not esPositivo(num)):
        print("Numero inválido.")
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
Método para mostrar el menú
'''
def menu():

    print("\n\t1. Diametro")
    print("\t2. Perímetro")
    print("\t3. Área")
    print("\t4. Salir")
    opcion = input("Eligue una opcion: ")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        opcion = -1
    return opcion

'''
Programa principal
'''
print("Vamos a calcular alguna propiedad de una circunferencia con el radio! ")
opcion = 0
while opcion != 4:
    opcion = menu()
    if( opcion == 1 ):
        num = pedirNumero()
        diametro = calculaDiametro(num)
        print(f"El diametro del circulo con radio {num} cm es {diametro:.2f} cm")
    elif( opcion == 3):
        num = pedirNumero()
        area = calculaArea(num)
        print(f"El área del circulo con radio {num} cm es {area:.2f} cm2")
    elif( opcion == 2):
        num = pedirNumero()
        perimetro = calculaPerimetro(num)
        print(f"El perimetro del circulo con radio {num} cm es {perimetro:.2f} cm")
    elif(opcion == 4):
        print("Hasta luego!!")
    else:
        print("Opcion no válida")

    
