# #########################################################
#  Ejercicio 4.5: Trabaja con una lista de números:
#  a) Crea una lista con números del 1 al 40. 
#  b) Muestra solo los números pares.
#  c) Muestra los números desde el último hasta el 17. 
#  d) Elimina el número 30.
#  e) Sustituye el número 30 por el texto "Jaime".
#  f) Añade una sublista [1, 'Manzana'] a la lista original y muestra la palabra "Manzana". 
#
#  Autor: Carla Cajal Pérez
# #########################################################
def esperar():
    resp = input("¿Quieres continuar? (s/n) ")
    while ( resp.lower() != 's'):
        resp = input("Ok, pulsa s cuando quieras continuar ")
    
    print("\nContinuemos!!")


print("Creo una lista con los numeros deñ 1 al 40!")
# a) Crear una lista con números del 1 al 40
numeros = list(range(1, 41))
print("Lista:", numeros)

esperar()

print("\nVoy a mostrarte solo los numeros pares")
# b) Mostrar solo los números pares
pares = []
for i in range(len(numeros)):
    if(i%2==0):
        pares.append(i)
print("Números pares:", pares)

esperar()

print("\nVoy a mostrarte los numeros del 40 al 17")
# c) Mostrar los números desde el último hasta el 17
numerosDesc = []
for num in reversed(numeros):
    if( num >= 17):
        numerosDesc.append(num) 
print("Números del último al 17:", numerosDesc)

esperar()

print("\nVoy a eliminar el numero 30 de la lista")
# d) Eliminar el número 30
copiaLista = numeros[:] #copia de la lista
copiaLista.remove(30)
print("Lista sin el 30:", copiaLista)

esperar()

print("\nVoy a sustituir el numero 30 de la lista")
# e) Sustituir el número 30 por "Jaime" (como ya lo eliminamos, lo añadimos en la posición 29)
indice = numeros.index(30)
if (numeros.index(30)):
    numeros[indice] = "Jaime"
print("Lista con 'Jaime' en lugar de 30:", numeros)

esperar()

print("\nVoy a añadir una sublista al final")
# f) Añadir una sublista [1, 'Manzana'] y mostrar "Manzana"
numeros.append([1, "Manzana"])
print("Lista con sublista añadida:", numeros)

print("\nAhora accedo al elemento")
print("Elemento a mostrar:", numeros[-1][1])


print("\n\nFIN DEL PROGRAMA")
