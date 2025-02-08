palabra = input("Dime una palabra: ")
opcion = -1
while opcion != 0:
print("¿Qué quieres hacer con la palabra?")
print("\t 1. Mostrar vocales (1)")
print("\t 2. Deletrear (2)")
print("\t 3. Primera y última letra (3)")
print("\t 0. Salir (0)")
opcion = input()
# comprobación
if opcion.isdigit():
opcion = int(opcion)
else:
opcion = -1
if ( opcion == 0 ):
print ("Hasta luego")
elif ( opcion == 1 ):
vocales = []
for i in palabra:
if( i in "aeiou"):
vocales.append(i)
print(f"Total: {len(palabra)}")
print(f"Vocales: {len(vocales)}")
print(f"Consonantes: {len(palabra) - len(vocales)}")
elif ( opcion == 2 ):
print(palabra[::-1])
elif ( opcion == 3 ):
print(palabra[0]+palabra[-1])
else:
print("Opción no válida")