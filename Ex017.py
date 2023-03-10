# Programa que recebe os valores dos catetos oposto e adjacente de um triangulo rectangulo e calcula e mostra o comprimento da sua hipotenusa
from math import hypot, sqrt

catOposto = float(input("Cateto Oposto = "))
catAdjacente = float(input("Cateto Adjacente = "))
print("Hipotenusa = {:.2f}\n".format(hypot(catOposto, catAdjacente)))
print("Hipotenusa = {:.2f}\n".format(sqrt((catOposto**2) + (catAdjacente**2))))