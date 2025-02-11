# método que dice si una variable es un numero o no
# si es numero returnea el numero y sino sigue pidiendo
# la introduccion de texto por teclado hasta que sea un numero
def esnumero(num):
    if(num.isdigit()):
        num = int(num)
    else:
        while( not num.isdigit()):
            print("Tamaño invalido")
            num = input("Vuelve a intentarlo: ")
        num = int(num)
    return num



print("Vamos a dibujar un rectángulo")
caracter = input("¿Con qué caracter quieres dibujarlo? ")
base = input("Dime el tamaño de la base: ")
base = esnumero(base)
altura = input("Dime el tamaño de la altura: ")
altura = esnumero(altura)
print(f"\nAquí tienes tu rectangulo de {base} * {altura}\n")
for i in range(altura):
    for j in range(base):
        print(caracter + " " , end="")
    print("\n") # no hace falta \n porque el print ya hace salto de linea