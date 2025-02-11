def pedirNumero():
    num = input("Inserta un número: ")
    
    while( not num.isdigit() ):
        print("Numero inválido.")
        num = input("Intentalo de nuevo: ")
    return float(num)
    
        
def menu():

    print("\n\t1. Suma")
    print("\t2. Resta")
    print("\t3. Multiplicación")
    print("\t4. División")
    opcion = input("Eligue una opcion:")
    if opcion.isdigit():
        opcion = int(opcion)
    else:
        opcion = -1
    return opcion

def suma( x, y):
    return x + y
    
def resta( x, y):
    return x-y

def multiplicar( x, y):
    return x*y

def dividir( x, y):
    return x/y


print("Binevenido a la calculadora de Carla")
continuar = "s"
while( continuar.lower() == "s" ):
    op = menu()
    if( op == 1):
        num1 = pedirNumero()
        num2 = pedirNumero()
        s = suma(num1,num2)
        print(f"La suma es: {s}")
    elif( op == 2):
        num1 = pedirNumero()
        num2 = pedirNumero()
        r = resta(num1,num2)
        print(f"La resta es: {r}")
    elif( op == 3):
        num1 = pedirNumero()
        num2 = pedirNumero()
        m = multiplicar(num1,num2)
        print(f"La multiplicacion es: {m}")
    elif( op == 4):
        num1 = pedirNumero()
        num2 = pedirNumero()
        d = dividir(num1,num2)
        print(f"La división es: {d}")
    else:
        print("Opcion no válida")
    continuar = input("\n¿Desea hacer otra operación? (s/n)")
if continuar.lower != "n":
    print("Opcion no válida, no se continuará ejecuntando el programa")
print("\n Gracias por usar la calculadora")
