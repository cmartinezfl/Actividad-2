# -*- coding: utf-8 -*-
"""Ejercicio Propuesto: 19"""

Lado=float(input("Valor lado triangulo"))

perimetro = Lado * 3
altura = (3**0.5 /2)*Lado
area = (3**0.5 /4) * Lado**2

print(f"El périmetro del triangulo es: {perimetro}, el valor de la altura: {altura:.2f} y el area del triangulo {area:.2f}")
