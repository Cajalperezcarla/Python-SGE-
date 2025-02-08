import math
numero1 = float(input("Dame un numero: "))
numero2 = float(input("Dame otro: "))
multiplicacion = numero1 * numero2
print("El producto es: " + str(multiplicacion))
if ( numero1 > numero2):
print("El numero 1 ("+str(numero1)+") es mayor")
elif ( numero2 > numero1):
print("El numero 2 ("+str(numero2)+") es mayor")
else:
print("Son iguales")
opcion = 0
while opcion != 1 and opcion !=2 :
opcion = int(input("Elige primero (1) o segundo (2): "))
if( opcion == 1):
cuadrado = float(numero1)**2
raiz = math.sqrt(float(numero1))
print("El cuadrado es: " + str(cuadrado))
print("La raiz es: " + str(raiz))
elif (opcion == 2):
cuadrado = float(numero2)**2
raiz = math.sqrt(float(numero2))
print("El cuadrado es: " + str(cuadrado))
print("La raiz es: " + str(raiz))
else:
print("Opción no válida, escoge otro numero")