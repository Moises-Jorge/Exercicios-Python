'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    1. Quantos números foram digitados.
    2. A lista de valores ordenada de forma decrescente.
    3. Se o valor 5 foi digitado e está ou não na lista.'''
lista_num = list()
while True:
    num = int(input('Digite um valor: '))
    lista_num.append(num)
    saida = str(input('Quer continuar?: ')).strip().upper()[0]
    while saida not in 'SN':
        saida = str(input('Quer continuar?: ')).strip().upper()[0]
    if saida == 'N':
        break
print('=-' * 30)
print(f'Voce digitou {len(lista_num)} numeros')
lista_num.sort(reverse=True)
print(f'Os valores em ordem decrescente sao: {lista_num}')
if 5 in lista_num:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 nao foi encontrado na lista!')