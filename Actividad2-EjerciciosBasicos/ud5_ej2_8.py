nums = [] # array pa guardar los numeros

enNumero = True
while enNumero:
    num = input("Introduce un número: ")
    
    if num.isdigit():  # Verificar si es un número
        nums.append(int(num))
    else:
        print("fin de la introduccion de numeros ")
        enNumero = False
    
if len(nums) > 0:
    print(f"Has introducido los números: {nums}")
    opcion = input("Dime un numero de la lista y te dire su posición")
    
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion in nums:
            posicion = nums.index(opcion) + 1  # Obtener la posición y sumar 1 para decir que es la posicion real
            print(f"La posición de {opcion} es {posicion}.")
        else:
            print(f"El número {opcion} no está en la lista.")

else:
    print("No has introducido ningún número.")   

