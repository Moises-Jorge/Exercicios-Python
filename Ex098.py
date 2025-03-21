'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
    1. De 1 até 10, de 1 em 1
    2. De 10 até 0, de 2 em 2
    3. Uma contagem personalizada.'''
from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} em {passo}')
    sleep(2.5)
    
    cont = inicio
    if cont <= fim:
        while cont <= fim:
            print(cont, end=' ', flush=True)
            sleep(.5)
            cont += passo
    else:
        while cont >= fim:
            print(cont, end=' ', flush=True)
            sleep(.5)
            cont -= passo
    print('FIM!')
    
    
# Programa Principal
contador(1,10,1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora eh sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(inicio, fim, passo)