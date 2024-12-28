'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
lista_num = list()
lista_pares = list()
lista_impares = list()
while True:
    lista_num.append(int(input('Digite um numero: ')))
    saida = str(input('Quer continuar?: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar?: ')).strip().upper()[0]
    if saida == 'N':
        break
for num in lista_num:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print('-=' * 30)
print(f'A lista completa eh: {lista_num}')
print(f'A lista de pares eh: {lista_pares}')
print(f'A lista de impares eh: {lista_impares}')