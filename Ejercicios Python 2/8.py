a1n1=int(input("Ingrese la primera calificacion: "))
a1n2=int(input("Ingrese la segunda calificacion: "))
a1n3=int(input("Ingrese la tercera calificacion: "))

if a1n1 > a1n3 and a1n2 > a1n3:
  a1nf =  a1n1 + a1n2
elif a1n1 > a1n2 and a1n3 > a1n2:
  a1nf = a1n1 +  a1n3
else: 
  a1nf = a1n2 + a1n3

a2n1=int(input("Ingrese la primera calificacion: "))
a2n2=int(input("Ingrese la segunda calificacion: "))
a2n3=int(input("Ingrese la tercera calificacion: "))

if a2n1 > a2n3 and a2n2 > a2n3:
  a2nf =  a2n1 + a2n2
elif a2n1 > a2n2 and a2n3 > a2n2:
  a2nf = a2n1 +  a2n3
else: 
  a2nf = a2n2 + a2n3

if a1nf > a2nf:
  print("El alumno 1 tiene una mejor calificacion final")
elif a1nf > a2nf:
  print("El alumno 2 tiene una mejor calificacion final")
else: 
  print("Ambos alumnos poseen la misma calificacion final")