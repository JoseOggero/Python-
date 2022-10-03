import string



SB = 100000
ANT = int(input("Ingrese sus años de antiguedad: "))
MP = 10000

AA = ANT * 0.012
BONOA = SB * AA

SN = SB + BONOA + MP

C = int(input("Ingrese 1 si esta casado o 0 de lo contrario: "))
CON = C * 800

H = int(input("Ingrese la cantidad de hijos que tiene: "))
HIJO = H * 400

ST = SN + CON + HIJO

print (ST)

AJ = SB * 0.11
OS = SB * 0.03
AG = SB * 0.01 

SF = ST - AJ - OS - AG

print ("Su Salario correspondiente es: ", SF)
