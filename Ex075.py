'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    1. Quantas vezes apareceu o valor 9.
    2. Em que posição foi digitado o primeiro valor 3.
    3. Quais foram os números pares.'''
numeros = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
           int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
# Mostrando os resultados
print('Voce digitou os valores: ', end='')
for num in numeros:
    print(f'{num} ', end='')
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
else:
    print('O valor 3 nao foi digitado em nenhuma posicao.')
# Mostrando os PARES
print('Os valores pares digitados foram: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(num, end=' ')
