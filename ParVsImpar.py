# INTRODUCE DIGITOS Y SEPARA POR PAR E IMPAR




digitos=input("introduce una secuencia de digitos: ")

digitos= [int(numeros)for numeros in digitos]



pares = [numeros for numeros in digitos if numeros % 2 == 0]
impares = [numeros for numeros in digitos if numeros % 2 != 0]



# Mostrar los resultados
print("Dígitos pares:", pares)
print("Dígitos impares:", impares)