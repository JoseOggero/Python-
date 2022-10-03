lista = []
cantidad = 3
mayor = 0 
menor = 0
i = 1

while (cantidad > 0):
    numero = float(input("Calificacion #" + str(i) + ": "))
    lista.append(numero)
    i = i +1
    cantidad = cantidad - 1

mayor = max(lista)
menor = min(lista)

print("Lista: ", lista)
print("Mayor: ", mayor)
print("Menor: ", menor)
