# Variables para almacenar los dos números anteriores
numAnt1 = 0  
numAnt2 = 0  

seguir = True

while seguir:
    # Pedir al usuario un número
    num = input("Introduce un número: ")

    # Verificar si la entrada es un número
    if num.isdigit():
        num = int(num)
        
        # Comprueba si el numero es menor que la suma de los dos anteriores
        if num < (numAnt1 + numAnt2):
            print(f"El número {num} es menor que la suma de los dos anteriores ({numAnt1} + {numAnt2}).")
            print("Fin del programa.")
            seguir = False  
        else:
            # Actualizar los valores de los números anteriores
            numAnt2 = numAnt1
            numAnt1 = num
    else:
        print("Introduce un número válido.")
