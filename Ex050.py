''' Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daquelas que forem pares. Se o valor digitado for ímpar, desconsidere-o. '''

soma = 0
for i in range(6):
    numero = int(input(f'Digite o {i+1} numero: '))
    if (numero % 2 == 0):
        soma += numero    
print(f'\nSoma dos pares: {soma}')