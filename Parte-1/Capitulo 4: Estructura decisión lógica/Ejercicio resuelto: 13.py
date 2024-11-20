compra= float(input("Valor compra: "))
color= input("Color bolita: ")
color= color.lower()

descuento=0

if color == "verde":
  descuento = 0.1*compra

elif color == "amarilla":
  descuento = 0.25*compra

elif color == "azul":
  descuento = 0.5*compra

elif color == "roja":
  descuento = 1*compra

elif color == "blanca":
  descuento = 0*compra

precio_final= compra-descuento

print(f"Dado que saco una bolita {color}, su compra valda {int(precio_final)} COP")
