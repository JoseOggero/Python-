from locale import DAY_2
import math

largo=int(input("Ingrese la longitud del bloque rectangular"))
ancho=int(input("Ingrese el ancho del bloque rectangular"))
alto=int(input("Ingrese la altura del bloque rectangular"))

d1 = math.sqrt(largo**2 + ancho**2)
d2 = math.sqrt(largo**2 + alto**2)
d3 = math.sqrt(ancho**2 + alto**2)

if d1 > d2 and d1 > d3: 
  print("Esta es la diagonal mas larga")
elif d2 > d1 and d2 > d3:
  print("Esta es la diagonal mas larga")
else:
  print("Esta es la diagonal mas larga")
