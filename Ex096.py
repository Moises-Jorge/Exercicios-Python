'''Faça um programa que tenha uma função chamada Área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''
def area(larg, comp):
    area = larg * comp
    print(f'A area de um terreno {larg} x {comp} eh de {area}m2.')


# Programa principal
print('Controle de Terrenos')
print('-' * 30)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)