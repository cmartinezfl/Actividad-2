nombre= input("Nombre: ")
horas= int(input("Horas trabajo: "))
valor= int(input("Valor por hora: "))

x=horas

if horas > 40:
  x= x-40
  if x > 8:
    x= x-8
    pago= 40*valor + 8*(2*valor) + x*(3*valor)

  else:
    pago= 40*valor + x*(2*valor)

else:
  pago= horas*valor

print(f"El pago semanal sera de {pago} COP")
