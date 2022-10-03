ckw = float(input("Ingrese la cantidad de kw consumidos: "))
pkw = float(input("ingrese el valor por kw: "))

if ckw > 700:
    e = ckw - 700
    cp = ((e * 1.05) + (ckw - e)) * pkw
    print("Su total a pagar es de: $",cp)
else:
    cp = ckw * pkw
    print("Su total a pagar es de: $",cp)

