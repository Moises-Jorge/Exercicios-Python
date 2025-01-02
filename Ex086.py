'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
for linha in range(3):
    for col in range(3):
        matriz[linha].append(int(input(f'Digite um valor para {[linha, col]}: ')))
print('-=' * 30)
for linha in matriz:
    for num in linha:
        print(f'[{num:^5}]', end='')
    print()