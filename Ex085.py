'''Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''
lista_principal = [[], []]
for i in range(7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0:
        lista_principal[0].append(num)
    else:
        lista_principal[1].append(num)
print('-=' * 30)
lista_principal[0].sort()
lista_principal[1].sort()
print(f'Os valores pares digitados foram: {lista_principal[0]}')
print(f'Os valores impares digitados foram: {lista_principal[1]}')
    