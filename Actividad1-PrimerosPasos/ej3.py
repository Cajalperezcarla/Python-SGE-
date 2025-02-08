numero = input("Escribe un numero positivo: ")
# funcion isdigit() --> true si es un digito, false si no lo es
while not numero.isdigit() or int(numero) <= 0 :
print("El caracter introducido no es un digito o no es valido")
numero = input("Prueba otra vez: ")
numero = int(numero) #convertimos a num, para evitar fallos
contador = 0 # contador de divisores
divisores = [] # almacen de divisores
for i in range(1, numero+1):
if numero % i == 0:
divisores.append(i)
contador += 1
print(f"El numero {numero} tiene {contador} divisores")
print(f"Sus divisores: {divisores}")
