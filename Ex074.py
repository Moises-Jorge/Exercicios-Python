'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
# maior = menor = 0
# Ciclo para achar o maior e o menor valor. Mas podemos usar as funcoes max() e min() para pegar o maior e o menor valor de uma tupla
""" for pos,num in enumerate(numeros):
    if pos == 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num """
print('Os valores sorteados foram: ', end='')
for num in numeros:
    print(f'{num} ', end='')
print(f'\nmaior = {max(numeros)}')
print(f'menor = {min(numeros)}')