''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
numero = int(input('Digite o numero: '))
tot_divisores = 0

for c in range(1, numero + 1): 
    if numero % c == 0:
        tot_divisores += 1

if tot_divisores == 2: # Um numero PRIMO soh tem 2 divisores: 1 e ele mesmo
    print(f'{numero} eh PRIMO')
else:
    print(f'{numero} NAO eh PRIMO')