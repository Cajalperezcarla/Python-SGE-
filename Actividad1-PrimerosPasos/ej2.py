opcion = "hola"
while( opcion != "par" and opcion != "impar"):
opcion = input("Elige par o impar: ")
lista = []
for i in range(1,1001):
if(opcion == "par") and ( i % 2 == 0):
lista.append(i)
elif(opcion == "impar") and (i%2 != 0):
lista.append(i)
print("Has elegido " + opcion )
print(lista)
print(f"Suma: {sum(lista)}")
print(f"Promedio: {sum(lista)/len(lista)}")