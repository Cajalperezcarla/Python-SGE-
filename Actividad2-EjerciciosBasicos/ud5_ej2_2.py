print("Piensa en un número entre 1 y 100, e intentaré adivinarlo.")

minimo = 1
maximo = 100
print("Responde con '+' si mi número es menor, '-' si es mayor, y '=' si he acertado.")

respuesta = "a"

while minimo <=maximo and respuesta != "=":
    
    num = (minimo + maximo) // 2
    print(f"¿Es {num} tu número?")
    respuesta = input("Responde (-/+/=): ")
    
    if respuesta == "=":
        print("¡HE GANADO!")
    elif respuesta == "-":
        maximo = num + 1
    elif respuesta == "+":
        minimo = num - 1
    else:
        print("Respuesta no válida")
        