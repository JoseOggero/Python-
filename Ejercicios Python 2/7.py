p=int(input("Ingrese 1 si quiere pasa de grados Farenheit a Centigrados o ingrese 2 dado el caso opuesto: ")) 
t=int(input("Ahora ingrese el digito de la temperatura: "))

if p == 1:
  c = 5 / 9 * (t - 32)
  print("La temperatura en Grados Centigrados es:", c,"°C")
else: 
 f = 32 + 9 * t / 5
 print("La temperatura en Gradios Farenheit es:", f,"°F")
