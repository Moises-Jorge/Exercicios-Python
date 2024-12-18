'''Crie um programa que simule o funcionamento de um caixa electrónico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    1. OBS: Considere que o caixa possui cédulas de 50, 20, 10 e 1.'''
print('=' * 30)
print(f"{'BANCO CEV':^30}")
print('=' * 30)
valor = int(input('Que valor quer sacar?: R$'))
ced = 50
tot_ced = 0
while True:
    if valor >= ced:
        valor -= ced
        tot_ced += 1
    else:
        if tot_ced > 0:
            print(f'Total de {tot_ced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot_ced = 0
        if valor == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV. Tenha um bom dia!!')