print("Voy a contar las vocales en el texto que introduzcas.")

texto = input("Introduce un texto: ")

contadorVocales = 0

vocales = "aeiouAEIOU"

# Recorremos el texto 
for caracter in texto:
    if caracter in vocales:  # buscamos las vocales
        contadorVocales += 1
        
print(f"El número de vocales en el texto es: {contadorVocales}")