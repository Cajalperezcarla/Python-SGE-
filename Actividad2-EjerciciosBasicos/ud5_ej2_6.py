# método que dice si una variable es un numero o no
# si es numero returnea el numero y sino sigue pidiendo
# la introduccion de texto por teclado hasta que sea un numero
def esnumero(num):
    if(num.isdigit()):
        num = int(num)
    else:
        while( not num.isdigit()):
            print("Número invalido")
            num = input("Vuelve a intentarlo: ")
        num = int(num)
    return num


print("Voy a calcularte los divisores del numero que introduzcas")
divisores = []
respuesta = "S"
while respuesta.upper() != "N":
    num = input("\nIntroduce un numero: ")
    num = esnumero(num)
    
    for i in range(num):
        if num % (i+1) == 0:
            divisores.append(i+1)
        
    print(f"Los divisores de {num} son: {divisores}")
    divisores.clear()
    
    respuesta = input("¿Quieres continuar? (S/N): ")
    while respuesta.upper() != "S" and respuesta.upper() != "N":  
        respuesta = input("No existe esa opción, responde con 'S' o 'N': ")
    
print("\nHasta luego!!!")
