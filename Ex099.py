'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* num):
    print('-=' * 30)
    print('Analisando os valores passados...')
    for n in num:
        print(n, end=' ', flush=True)
        sleep(.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) != 0:
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print(f'O maior valor informado foi 0.')


# Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()