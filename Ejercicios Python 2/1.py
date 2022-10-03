from cmath import pi
import math

r=int(input("Ingrese el valor de el RADIO de un cilindro: "))
a=int(input("Ingrese el valor de la Altura de un cilindro: "))

if a > r:
    v = 2 * math.pi * r * (a + r)
    print("El volumen del cilindro es: ",v)
else:
    area = math.pi * (r**2) * a
    print("El area del cilindro es ",area)