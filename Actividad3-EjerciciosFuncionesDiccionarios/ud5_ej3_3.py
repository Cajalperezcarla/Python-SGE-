#########################################################
#  Programa que encuentra los elementos comunes entre 
#  dos listas dadas.
#########################################################

'''
Función que toma dos listas como parámetros y devuelve
una lista con los elementos comunes entre ambas.
'''
def elementosComunes(lista1, lista2):
    # Convertimos ambas listas en conjuntos y usamos la intersección
    return list(set(lista1) & set(lista2))

'''
Función para pedir una lista al usuario.
'''
def pedirLista(nombre):
    lista = []
    print(f"Introduce números para la {nombre} (escribe 'n' para terminar):")
    entrada = 'x'
    while entrada != 'n':
        entrada = input("Introduce un número: ")
        if entrada != 'n' and entrada.isdigit():
            lista.append(int(entrada))
        elif entrada != 'n':
            print("Caracter no válido. Por favor, introduce un número.")
    return lista

'''
Programa principal
'''
print("Vamos a encontrar los elementos comunes entre dos listas.")

# Pedir las dos listas al usuario
lista1 = pedirLista("primera lista")
lista2 = pedirLista("segunda lista")

# Obtener los elementos comunes
comunes = elementosComunes(lista1, lista2)

# Mostrar los resultados
print(f"\nPrimera lista: {lista1}")
print(f"Segunda lista: {lista2}")
print(f"Elementos comunes: {comunes}")
