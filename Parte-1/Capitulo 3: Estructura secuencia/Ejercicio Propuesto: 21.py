Lado_1=float(input("Valor lado 1 triangulo: "))
Lado_2=float(input("Valor lado 2 triangulo: "))
Lado_3=float(input("Valor lado 3 triangulo: "))

perimetro= Lado_1+Lado_2+Lado_3
semiperimetro= perimetro/2
s=semiperimetro
area= (s*(s - Lado_1)*(s - Lado_2)*(s - Lado_3))**0.5

print("Perimetro: ", perimetro)
print("Semiperimetro: ", semiperimetro)
print(f"Area: {area:.2f}")
