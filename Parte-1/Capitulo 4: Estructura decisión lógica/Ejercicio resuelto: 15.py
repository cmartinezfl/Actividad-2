A=float(input("Peso bola A: "))
B=float(input("Peso bola B: "))
C=float(input("Peso bola C: "))
D=float(input("Peso bola D: "))

bolas=[A, B, C, D]
iguales=[]
diferente=[]3

for i in range(len(bolas)):
  bola=bolas[i]

  for j in range(0,4):
    if bola == bolas[j] and i != j:
      iguales.append(bola)

  if bola not in iguales:
    diferente.append(bola)

if diferente[0] < iguales[0]:
  comparacion= "menor"

elif diferente[0] > iguales[0]:
  comparacion= "mayor"

if diferente[0]==A:
  print(f"A es la esfera diferente y tiene un peso {comparacion} a las otras")

if diferente[0]==B:
  print(f"B es la esfera diferente y tiene un peso {comparacion} a las otras")

if diferente[0]==C:
  print(f"C es la esfera diferente y tiene un peso {comparacion} a las otras")

if diferente[0]==D:
  print(f"D es la esfera diferente y tiene un peso {comparacion} a las otras")
