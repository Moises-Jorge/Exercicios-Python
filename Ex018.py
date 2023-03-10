# Programa que leh um angulo qualquer e mostra o seno, cosseno e a tangente do mesmo
from math import sin, cos, tan

angulo = float(input("Informe o angulo: "))
print("Seno de {}º = {}".format(angulo, sin(angulo)))
print("Cos de {}º = {}".format(angulo, cos(angulo)))
print("Tan de {}º = {}\n".format(angulo, tan(angulo)))