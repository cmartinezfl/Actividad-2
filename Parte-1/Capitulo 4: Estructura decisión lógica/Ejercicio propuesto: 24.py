a= float(input("Peso de la esfera A: "))
b= float(input("Peso de la esfera B: "))
c= float(input("Peso de la esfera C: "))

esferas=[a, b, c]
letras=["A", "B", "C"]

mayor = max(esferas)

indice= esferas.index(mayor)

MAYOR= letras[indice]

print(f"La esfera {MAYOR} es la esfera de mayor peso")
