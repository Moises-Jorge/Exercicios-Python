'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''
lista_num = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in lista_num:
        lista_num.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Nao vou adicionar...')
    saida = str(input('Quer continuar?: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar?: ')).strip().upper()[0]
    if saida == 'N':
        break
print('-=' * 30)
lista_num.sort()
print(f'Voce digitou os valores {lista_num}')
