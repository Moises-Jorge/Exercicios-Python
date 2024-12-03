''' Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. '''
numero = int(input('Digite o numero: '))

if numero <= 1:
    print(f'{numero} nao eh primo')
else:
    primo = True
    