#########################################################
#  Programa que invierte una cadena usando una función.
#########################################################

'''
Función que recibe una cadena y devuelve la misma cadena
en orden inverso.
'''
def invertirCadena(cadena):
    return cadena[::-1]

'''
Programa principal
'''
print("Vamos a invertir una cadena.")

# Pedir la cadena al usuario
cadena = input("Introduce una cadena: ")

# Llamar a la función para invertir la cadena
cadenaInvertida = invertirCadena(cadena)

# Mostrar el resultado
print(f"\nLa cadena original es: {cadena}")
print(f"La cadena invertida es: {cadenaInvertida}")
