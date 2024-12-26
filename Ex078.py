'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista.'''
numeros = list()
maior = menor = 0
# Sem funcoes de manipulacao de listas (no braco)
for i in range(5):
    numeros.append(int(input(f'Digite o {i+1}º numero: ')))
    """ if i == 0:
        maior = menor = numeros[i]
    elif numeros[i] > maior:
        maior = numeros[i]
    elif numeros[i] < menor:
        menor = numeros[i]
print('=-' * 40)
print(f'Voce digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posicoes: ', end='')
for pos, valor in enumerate(numeros):
    if valor == maior:
        print(pos, end=' ')
print(f'\nO menor valor digitado foi {menor} nas posicoes: ', end='')
for pos, valor in enumerate(numeros):
    if valor == menor:
        print(pos, end=' ') """
# Usando funcoes ja prontas para manipular listas
print('=-' * 40)
maior = max(numeros)
menor = min(numeros)
print(f'O maior valor digitado foi {maior} nas posicoes: ', end='')
for pos, valor in enumerate(numeros):
    if valor == maior:
        print(pos, end=' ')
print(f'\nO menor valor digitado foi {menor} nas posicoes: ', end='')
for pos, valor in enumerate(numeros):
    if valor == menor:
        print(pos, end=' ')

