numero_inscripcion= int(input("Ingrese el numero de inscripcion: "))
nombres= input("Ingrese los nombres: ")
patrimonio= int(input("Ingrese su patrimonio: "))
estrato= int(input("Ingrese su estrato: "))

cobro_base= 50000
adicion=0

if patrimonio > 2000000 and estrato > 3:
  adicion= patrimonio * 0.03

cobro_final= cobro_base + adicion

print("Numero de inscripcion: ", numero_inscripcion)
print("Nombres: ", nombres)
print("Pago por matricula: ", cobro_final)
