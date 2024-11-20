nombre=input("Ingrese el nombre del trabajador: ")
salario=float(input("Ingrese el salario por hora trabajada: "))
horas=int(input("Ingrese las horas trabajadas en el mes: "))

salario_final= salario * horas

print(f"Trabajador: {nombre}")

if salario_final > 450000:
  print(f"Salario mensual: {int(salario_final)} COP")
