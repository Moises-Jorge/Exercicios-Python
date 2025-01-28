'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint
from time import sleep


def sorteia(lista_num):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        num = randint(1, 10)
        print(num, end=' ', flush=True)
        sleep(.4)
        lista_num.append(num)
    print('PRONTO!')


def soma_par(lista_num):
    res_soma_par = 0
    for num in lista_num:
        if num % 2 == 0:
            res_soma_par += num
    print(f'Somando os valores pares de {lista_num}, temos {res_soma_par}')


# Programa Principal
numeros = list()
sorteia(numeros)
soma_par(numeros)