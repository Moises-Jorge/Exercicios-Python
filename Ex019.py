# Programa que leh quatro nomes e sortea um deles para realizar uma tarefa
from random import choice

primeiro = str(input("Primeiro nome: "))
segundo = str(input("Segundo nome: "))
terceiro = str(input("Terceiro nome: "))
quarto = str(input("Quarto nome: "))

lista = [primeiro, segundo, terceiro, quarto]

print("O nome escolhido foi: {}\n".format(choice(lista)))