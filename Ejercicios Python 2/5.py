n = float(input("Ingrese un numero: "))

entero = n % 1

if entero == 0 and n % 7 == 0:
    print("El numero ",n , "es entero y multiplo de 7")
elif entero == 0:
    print("El numero ",n , "es entero y NO es multiplo de 7")
elif n % 7 == 0:
    print("El numero ",n , " NO es entero y es multiplo de 7")
else:
    print("El numero ",n , " NO es entero y NO es multiplo de 7") 


