# -*- coding: utf-8 -*-
"""Ejercicio propuesto: 24

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WWAI3IkwbI11VPKQ2uygSEKIH9m8VFqL
"""

a= float(input("Peso de la esfera A: "))
b= float(input("Peso de la esfera B: "))
c= float(input("Peso de la esfera C: "))

esferas=[a, b, c]
letras=["A", "B", "C"]

mayor = max(esferas)

indice= esferas.index(mayor)

MAYOR= letras[indice]

print(f"La esfera {MAYOR} es la esfera de mayor peso")