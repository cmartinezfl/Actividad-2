a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

x = -b
y_1 = (b**2) - (4*a*c)

if y_1 < 0:
  print("La solucion pertenece a los numeros complejos")

else:
  y = (y_1)**0.5
  z = 2*a

  solucion_1 = (x + y)/z
  solucion_2 = (x - y)/z

  print("Solucion 1: ", solucion_1)
  print("Solucion 2: ", solucion_2)
