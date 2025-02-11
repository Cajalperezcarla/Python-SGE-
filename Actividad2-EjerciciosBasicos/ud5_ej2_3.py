impares = []
while len(impares) < 3:
    
    num = input("Introduce un numero: ")
    if num.isdigit():
        num = float(num)
    else:
        while not num.isdigit():
            print("El caracter no es un numero")
            num = input("Introduce un numero")
        num = float(num)
    
    if ( num % 2 != 0):
        impares.append(num)
        print("Has introducido un numero impar")
    else:
        print(f"Has introducido un numero par")
        
print("Has introducido 3 numeros impares")
    
    