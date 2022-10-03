c1 = int(input("Ingrese su primera calificacion: "))
c2 = int(input("Ingrese su segunda calificacion: "))
c3 = int(input("Ingrese su tercera calificacion: "))

if c1 > c2 and c1 > c3:
    if c2 > c3:
        print("Su calificacion mas alta es: ",c1," y su calificacion mas baja es: ", c3)
    else:
        print("Su calificacion mas alta es: ",c1," y su calificacion mas baja es: ", c2)
elif c2 > c1 and c2 > c3:
    if c1 > c3:
        print("Su calificacion mas alta es: ",c2," y su calificacion mas baja es: ", c3)
    else:
        print("Su calificacion mas alta es: ",c2," y su calificacion mas baja es: ", c1)
elif c3 > c1 and c3 > c2:
    if c1 > c2:
        print("Su calificacion mas alta es: ",c3," y su calificacion mas baja es: ", c2)
    else:
        print("Su calificacion mas alta es: ",c3," y su calificacion mas baja es: ", c1)
else:
    print("Error")