departamento_1= float(input("Ventas departamento 1: "))
departamento_2= float(input("Ventas departamento 2: "))
departamento_3= float(input("Ventas departamento 3: "))

salario= float(input("Salario vendedores: "))

salario_d1= salario
salario_d2= salario
salario_d3= salario

ventas= departamento_1 + departamento_2 +  departamento_3

tercio= ventas*0.33

if departamento_1 > tercio:
  salario_d1= salario + (salario*0.2)

if departamento_2 > tercio:
  salario_d2= salario + (salario*0.2)

if departamento_3 > tercio:
  salario_d3= salario + (salario*0.2)

salarios=[salario_d1, salario_d2, salario_d3]

for i in range(0,3):
  x= i+1
  print(f"El salario del departamento {x} sera de {int(salarios[i])} COP")
