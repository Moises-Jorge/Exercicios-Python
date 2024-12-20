''' Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezasseis', 'Dezassete', 'Dezoito', 'Dezanove', 'Vinte')

""" num = int(input('Digite um numero entre 0 e 20: '))
while num < 0 or num > 20:
    num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Voce digitou o numero {num_extenso[num]}') """

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o numero: {num_extenso[num]}')
    cond_saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while cond_saida not in 'SN':
        cond_saida = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cond_saida == 'N':
        break