'''Rescreva a função leia_int() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um numero invalido. Aproveite e crie também uma função leia_float() com a mesma funcionalidade.'''
from modulos.uteis.numeros import leia_int, leia_float
        


# programa principal
numero = leia_int('Digite um Inteiro: ')
numero2 = leia_float('Digite um Real: ')
print(f'O numero inteiro digitado foi {numero} e o real foi {numero2}')