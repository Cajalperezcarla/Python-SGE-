# #########################################################
#  Ejercicio 4.2: Pide al usuario que introduzca un valor 
#  numérico por pantalla y luego suma dicho número a 2.
#  Explica qué sucede y por qué
#
#  Autor: Carla Cajal Pérez
# #########################################################

# Solicitar un número al usuario
numero = input("Introduce un número: ")

# Intentamos sumarle 2
resultado = numero + 2

# Mostrar el resultado
print(f"El resultado es: {resultado}")

'''
si ponemos el código anterior, fallará,
porque interpreta la variable numero como 
string y no es capaz de sumar un string con un int.
Por lo que antes de realizar la suma habrá que
cambiar el valor de numero a un float (por ejemplo)

-----------------------------------------------------

numero = float(input("Introduce un número: "))
resultado = numero + 2
print(f"El resultado es: {resultado}")

-----------------------------------------------------

'''