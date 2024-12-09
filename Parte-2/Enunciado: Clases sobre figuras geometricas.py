import math

class Cir:

  def __init__(self, radio):
    self.radio = radio

  def hallar_perimetro(self):
    self.perimetro = 2 * math.pi * self.radio

  def hallar_area(self):
    self.area = math.pi * (self.radio ** 2)

r=float(input("Ingrese el radio del circulo: "))

circulo = Cir(r)

circulo.hallar_perimetro()
circulo.hallar_area()

print(f"El circulo tiene perimetro: {round(circulo.perimetro,2)} cm y un area de {round(circulo.area,2)} cm")

print("")

class Rec:

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def hallar_perimetro(self):
    self.perimetro = (2*self.base)+(2*self.altura)

  def hallar_area(self):
    self.area = self.base * self.altura

b=float(input("Ingrese la base del rectangulo: "))
a=float(input("Ingrese la altura del rectangulo: "))

rectangulo = Rec(b, a)

rectangulo.hallar_perimetro()
rectangulo.hallar_area()

print(f"El rectangulo tiene perimetro: {round(rectangulo.perimetro,2)} cm y un area de {round(rectangulo.area,2)} cm")

print("")


class Cua:

  def __init__(self, lado):
    self.lado = lado

  def hallar_perimetro(self):
    self.perimetro = self.lado*4

  def hallar_area(self):
    self.area = self.lado**2

l=float(input("Ingrese el lado del cuadrado: "))

cuadrado = Cua(l)

cuadrado.hallar_perimetro()
cuadrado.hallar_area()

print(f"El cuadrado tiene perimetro: {round(cuadrado.perimetro,2)} cm y un area de {round(cuadrado.area,2)} cm")

print("")


class Tri:

  def __init__(self, base, altura):
    self.base = base
    self.altura = altura
    self.hipotenusa = None
    self.tipo = None

  def hallar_area(self):
    self.area = (1/2) * self.base * self.altura

  def hallar_hipotenusa(self):
    self.hipotenusa = math.sqrt((self.base**2) + (self.altura**2))

  def hallar_perimetro(self):
    self.perimetro = self.altura + self.base + self.hipotenusa

  def hallar_tipo(self):
    if self.hipotenusa == self.base == self.altura:
      self.tipo = "Equilatero"

    elif self.hipotenusa != self.base != self.altura:
      self.tipo = "Escaleno"

    else:
      self.tipo = "Isosceles"

bt= float(input("Ingrese la base del triangulo rectangulo: "))
at= float(input("Ingrese la altura del triangulo rectangulo: "))

triangulo = Tri(bt, at)

triangulo.hallar_hipotenusa()
triangulo.hallar_perimetro()
triangulo.hallar_area()
triangulo.hallar_tipo()

print(f"El triangulo tiene perimetro: {round(triangulo.perimetro,2)} cm y un area de {round(triangulo.area,2)} cm")
print(f"Adémas, tiene hipotenusa: {round(triangulo.hipotenusa,2)} cm y es un triangulo {triangulo.tipo}")
