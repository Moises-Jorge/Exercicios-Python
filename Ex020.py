# Progrma que leh o nome de quatro de alunos e mostre a ordem de apresentacao de um determinado trabalho
from random import shuffle

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print("A ordem de apresentacao sera: {}\n".format(lista))