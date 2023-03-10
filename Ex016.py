# Programa que leh um numero real qualquer e mostra na tela somente a parte inteira deste numero
from math import trunc

num = float(input("Digite um numero com casas decimais: "))
print("Parte inteira do numero digitado: {}\n".format(trunc(num)))