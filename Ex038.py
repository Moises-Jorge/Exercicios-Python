# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor eh o maior, O segundo valor eh o maior, os dois valores sao iguais

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if n1 > n2:
    print("O primeiro valor eh maior!")
elif n2 > n1:
    print("O segundo valor eh maior!")
else:
    print("Nao existe valor maior, os dois sao iguais!")
