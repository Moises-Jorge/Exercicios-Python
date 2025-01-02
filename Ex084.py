'''Faça um programa que leia o nome e o peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
    1. Quantas pessoas foram cadastradas.
    2. Uma listagem com as pessoas mais pesadas
    3. Uma listagem com as pessoas mais leves.'''
pessoas = list()
dado_pessoa = list()
maior = menor = 0
while True:
    dado_pessoa.append(str(input('Nome: ')))
    dado_pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dado_pessoa[1]
    elif dado_pessoa[1] > maior:
        maior = dado_pessoa[1]
    elif dado_pessoa[1] < menor:
        menor = dado_pessoa[1]
    pessoas.append(dado_pessoa[:])
    dado_pessoa.clear()
    saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if saida == 'N':
        break
print('-=' * 30)
print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi: {maior}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end='')
print(f'\nO menor peso foi: {menor}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end='')
