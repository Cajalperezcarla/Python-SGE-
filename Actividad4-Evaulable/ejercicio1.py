# #########################################################
#  Ejercicio 4.1: Ordena una lista de números de menor a mayor
#  sin usar la función sort(). La lista inicial es:
#  [5.55, math.pi, math.sqrt(2), 200, -35.55, 1/3, 0.333333333]
#
#  Autor: Carla Cajal Pérez
# #########################################################
import math
'''
Método que ordena la lista que se le pasa por parámetro
'''
def ordena(lista):
    lista_ordenada = []
    while lista:
        minimo = lista[0]
        for i in lista:
            if i < minimo:
                minimo = i
        lista_ordenada.append(minimo)
        lista.remove(minimo)
    return lista_ordenada
    

'''
Programa principal
'''
list = [5.55, math.pi, math.sqrt(2), 200, -35.55, 1/3, 0.333333333]
print("Hola, vamos a ordenar la siguiente lista de mayor a menor!!!")
print(f" {list}")

print(f"La lista ordenada es {ordena(list)}")


