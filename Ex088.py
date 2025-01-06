'''Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista compostas.'''
from random import randint
from time import sleep
print('-' * 30)
print('     JOGA NA MEGA SENA       ')
print('-' * 30)
qtd_jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
lista_jogos = list()
lista_numeros = list()
for jogo in range(qtd_jogos):
    for n in range(6):
        numero = randint(1, 60)
        if numero not in lista_numeros:
            lista_numeros.append(numero)
    lista_numeros.sort()
    lista_jogos.append(lista_numeros[:])
    lista_numeros.clear()
print('-=' * 3, f' SORTEANDO {qtd_jogos} JOGOS ', '-=' * 3)
for index, jogo in enumerate(lista_jogos):
    print(f'Jogo {index+1}: {jogo}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)