numeros=[]

for i in range(1,4):
  n=int(input(f"ingrese el numero {i}: "))
  numeros.append(n)

mayor= max(numeros)

print("El mayor es: ", mayor)
