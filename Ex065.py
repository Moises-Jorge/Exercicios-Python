''' Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os os valores e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores. '''
soma_valores = total_valores = maior = menor = 0
cond_saida = 'S'
while cond_saida in 'S':
    num = int(input('Digite um numero: '))
    total_valores += 1
    soma_valores += num
    
    if total_valores == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

    cond_saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while cond_saida not in 'NS':
        print('RESPOSTA ERRADA!')
        cond_saida = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
print(f'\nVoce digitou {total_valores} numeros\nA soma entre eles eh: {soma_valores}\nA media entre todos os valores foi: {soma_valores/total_valores: .2f}')
print(f'O maior valor foi: {maior}\nO menor valor foi: {menor}')