codigo=int(input("Código empleado:"))
nombres=input("Nombres:")
horas_mes=int(input("Horas de trabajo (mes):"))
valor_hora=int(input("Valor por hora de trabajo:"))
porcentaje_retencion=float(input("Porcentaje de retencion: "))

retencion= (horas_mes*valor_hora) * (porcentaje_retencion/100)

salario_bruto= horas_mes*valor_hora
salario_neto= int(salario_bruto - retencion)

print(f"Código: {codigo}")
print(f"Nombres: {nombres}")
print(f"Salario bruto: {salario_bruto}")
print(f"Salario neto: {salario_neto}")
