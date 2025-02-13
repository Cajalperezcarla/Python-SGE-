# #########################################################
#  Ejercicio 4.7: Escribe un programa que:
#       1. Reciba una cadena de caracteres y devuelva un 
#       diccionario con cada palabra que contiene y su frecuencia.
#       2. Reciba el diccionario generado y devuelva una 
#       tupla con la palabra más repetida y su frecuencia.
#
#  Autor: Carla Cajal Pérez
# #########################################################
'''
Método que cuenta las palabras repetidas de un texto y 
devuelve un diccionario con la cantidad de apariciones 
de cada palabra
'''
def contarPalabras(texto):
    palabras = texto.lower().split()  # Convertir todo a minúsculas y separar palabras
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia
'''
Método que devuelve entre lel 
contador de las palabra, cual es la que mas ha aparecido
'''
def palabraMasRepetida(frecuencia):
    if not frecuencia:
        return None  # Si el diccionario está vacío, no devuelve nada
    
    palabraMasFrecuente = None # almacena la palara que aparece más veces
    frecuenciaMaxima = 0 #almacena el maximo de veces que apaerce la palabra mas aparecida
    
    for palabra, cantidad in frecuencia.items():
        if cantidad > frecuenciaMaxima:
            frecuenciaMaxima = cantidad
            palabraMasFrecuente = palabra
            
    return (palabraMasFrecuente, frecuenciaMaxima)

'''
Programa principal
'''
texto = input("Introduce una cadena de texto: ")
palabras = contarPalabras(texto)
print("Frecuencia de palabras:", palabras)

palabraMasRepetida = palabraMasRepetida(palabras)
if palabraMasRepetida:
    print(f"La palabra más repetida es '{palabraMasRepetida[0]}' con {palabraMasRepetida[1]} apariciones.")
else:
    print("No se encontraron palabras en el texto.")