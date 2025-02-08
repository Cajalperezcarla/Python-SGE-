# Función para sumar 2 números
def SumaDosNumeros(a, b):
return a + b
# Función para sumar una lista de números
def SumarLista(nums):
return sum(nums)
# Programa principal
opcion = -1
while opcion != 0:
print("\n¿Qué quieres hacer?")
print("\t 1. Sumar dos números (1)")
print("\t 2. Sumar lista de números (2)")
print("\t 0. Salir (0)")
opcion = input("Elige una opción: ")
# Comprobación de que la opción sea válida
if opcion.isdigit():
opcion = int(opcion)
else:
opcion = -1
# opciones del menu
if opcion == 0:
print("¡Hasta luego!")
elif opcion == 1:
# Pedir dos números
num1 = float(input("Dame el primer número: "))
num2 = float(input("Dame el segundo número: "))
resultado = SumaDosNumeros(num1, num2)
print(f"La suma de {num1} y {num2} es: {resultado}")
elif opcion == 2:
lista = []
num = ""
# crear lista
while num != ".":
num = input("Introduce un número (o '.' para terminar): ")
if num.isdigit():
lista.append(float(num))
elif num != ".":
print("Por favor, ingresa un número válido")
resultado = SumarLista(lista)
print(f"La suma de los números en la lista es: {resultado}")
else:
print("Opción no válida")