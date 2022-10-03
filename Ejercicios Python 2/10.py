l1 = int(input("Ingrese el largo del lado del triangulo: "))
l2 = int(input("Ingrese el largo del lado del triangulo: "))
l3 = int(input("Ingrese el largo del lado del triangulo: "))

if l1 == l2 and l1 == l3:
    print("El triangulo es Equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("El triangulo es Isosceles")
else:
    print("El triangulo es Escaleno")